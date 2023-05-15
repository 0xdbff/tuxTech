from django.db import models, transaction
from django.db import IntegrityError
from django.utils import timezone
from datetime import timedelta
from enum import Enum
from django.core.mail import EmailMessage
from django.db.models import Sum

import uuid


class OrderStatus(Enum):
    """
    An enumeration representing the possible statuses of an order.
    """

    CREATED = "Created"
    PAYMENT_PENDING = "Payment Pending"
    PAYMENT_CONFIRMED = "Payment Confirmed"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

    @classmethod
    def choices(cls):
        """
        Get a list of tuples representing the possible choices for an order's status.
        This can be used for a Django model field.

        Returns:
            list: A list of tuples where each tuple contains a status value and status name.
        """
        return [(key.value, key.name) for key in cls]


class DeliveryOption(Enum):
    """
    An enumeration representing the possible delivery options for an order.

    Attributes:
        CTT: Delivery by CTT service.
        DHL: Delivery by DHL service.
        UPS: Delivery by UPS service.
    """

    CTT = "CTT"
    DHL = "DHL"
    UPS = "UPS"

    @classmethod
    def choices(cls):
        """
        Get a list of tuples representing the possible choices for an order's delivery option.
        This can be used for a Django model field.

        Returns:
            list: A list of tuples where each tuple contains a delivery option value and name.
        """
        return [(key.value, key.name) for key in cls]


class OrderedItem(models.Model):
    """
    A model representing an item in an order.
    """

    order = models.ForeignKey(
        "order.Order", related_name="ordered_items", on_delete=models.CASCADE
    )
    product_variant = models.ForeignKey("product.Variant", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        """
        Save the ordered item. If the item already exists, the old units are returned to the stock.
        If there's not enough stock for the product variant, an IntegrityError is raised.

        Raises:
            IntegrityError: If there's not enough stock for this product variant.
        """
        if self.pk:  # If this item already exists in the database
            old_self = OrderedItem.objects.get(pk=self.pk)
            self.product_variant.units.filter(
                order=old_self.order
            ).delete()  # Return the old units to stock

        available_units = self.product_variant.units.filter(order__isnull=True)
        if available_units.count() < self.quantity:
            raise IntegrityError("Not enough stock for this product variant")

        self.order.calculate_total_cost()

        super().save(*args, **kwargs)

        for unit in available_units[: self.quantity]:
            unit.order = self.order
            unit.save()

    @property
    def total_price(self):
        """
        Calculate the total price for this ordered item.

        Returns:
            Decimal: The total price.
        """
        return self.product_variant.price * self.quantity


class Order(models.Model):
    """
    A model representing an order.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4().hex)
    customer = models.ForeignKey("users.TuxTechUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices(), default=OrderStatus.CREATED.value
    )
    shipping_address = models.ForeignKey(
        "users.Address",
        related_name="shipping_orders",
        on_delete=models.SET_NULL,
        null=True,
    )
    billing_address = models.ForeignKey(
        "users.Address",
        related_name="billing_orders",
        on_delete=models.SET_NULL,
        null=True,
    )
    payment_info = models.TextField(null=True)
    shipped_at = models.DateTimeField(null=True)
    include_nif = models.BooleanField(null=False, default=True)
    delivery_option = models.CharField(
        max_length=10,
        choices=DeliveryOption.choices(),
        default=DeliveryOption.CTT.value,
    )

    def confirm_payment(self):
        """
        Confirm the payment for the order.
        """
        with transaction.atomic():
            self.status = OrderStatus.PAYMENT_CONFIRMED.value
            self.save()

    def ship(self):
        """
        Ship the order.

        Raises:
            ValueError: If the order hasn't been paid for.
        """
        with transaction.atomic():
            if self.status != OrderStatus.PAYMENT_CONFIRMED.value:
                raise ValueError("Cannot ship an order that hasn't been paid for.")
            self.status = OrderStatus.SHIPPED.value
            self.save()

    def deliver(self):
        """
        Deliver the order.

        Raises:
            ValueError: If the order hasn't been shipped.
        """
        with transaction.atomic():
            if self.status != OrderStatus.SHIPPED.value:
                raise ValueError("Cannot deliver an order that hasn't been shipped.")
            self.status = OrderStatus.DELIVERED.value
            self.save()

    def cancel(self):
        """
        Cancel the order.

        Raises:
            ValueError: If the order has been shipped or delivered.
        """
        with transaction.atomic():
            if self.status not in [
                OrderStatus.SHIPPED.value,
                OrderStatus.DELIVERED.value,
            ]:
                self.status = OrderStatus.CANCELLED.value
                self.save()
            else:
                raise ValueError(
                    "Cannot cancel an order that has been shipped or delivered."
                )

    def save(self, *args, **kwargs):
        """
        Save the order. Depending on the order's state, it might be marked as delivered,
        shipped or payment confirmed. If the status changes, an update email is sent.

        Raises:
            ValueError: If the order has been shipped or delivered.
        """
        # If the order has been shipped and it's been 24 hours, mark it as delivered
        if self.shipped_at and timezone.now() - self.shipped_at >= timedelta(hours=24):
            self.status = OrderStatus.DELIVERED.value
        # If all items are in stock, mark the order as shipped
        elif all(
            models.OrderedItem.objects.filter(order=self)
            .product_variant.units.filter(order__isnull=True)
            .count()
            >= models.OrderedItem.objects.filter(order=self).quantity
        ):
            self.status = OrderStatus.SHIPPED.value
            self.shipped_at = timezone.now()
            # !TODO integrate with transportation services
            self.status = OrderStatus.DELIVERED.value
        # If payment information has been provided, mark the order as payment confirmed
        elif self.payment_info:
            self.status = OrderStatus.PAYMENT_CONFIRMED.value
            # Update paid_at timestamp if it hasn't been set
            if not self.paid_at:
                self.paid_at = timezone.now()

        if self.pk is not None:
            old_order = Order.objects.get(pk=self.pk)

            if old_order.status != self.status:
                self.send_status_update_email()

        super().save(*args, **kwargs)

    def send_status_update_email(self):
        """
        Send an email to the customer to update them about the status of their order.
        """

        email_subjects_messages = {
            OrderStatus.CREATED.value: (
                "Your Order Has Been Created",
                "Your order has been successfully created and we are preparing it for shipment.",
            ),
            OrderStatus.PAYMENT_PENDING.value: (
                "Payment For Your Order Is Pending",
                "We are awaiting payment for your order.",
            ),
            OrderStatus.PAYMENT_CONFIRMED.value: (
                "Payment For Your Order Confirmed",
                "We have received your payment and your order will be shipped soon.",
            ),
            OrderStatus.SHIPPED.value: (
                "Your Order Has Been Shipped",
                "Your order has been shipped and is on its way.",
            ),
            OrderStatus.DELIVERED.value: (
                "Your Order Has Been Delivered",
                "Your order has been successfully delivered.",
            ),
            OrderStatus.CANCELLED.value: (
                "Your Order Has Been Cancelled",
                "Your order has been cancelled.",
            ),
        }

        subject, message = email_subjects_messages.get(
            self.status, ("Order Update", "Your order status has been updated.")
        )

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email="home@gldb.dev",
            to=[self.customer.email],
        )
        email.send()

    def calculate_total_cost(self):
        """
        Calculate the total cost of the order by summing up the total cost of each ordered item.
        """
        self.total_cost = sum(item.total_price for item in self.ordered_items.all())
        self.save()

    @staticmethod
    def sales_growth(start_date, end_date):
        """
        Calculate sales growth between two dates.

        Args:
            start_date (datetime): The start date.
            end_date (datetime): The end date.

        Returns:
            float: The sales growth as a percentage.
        """
        previous_period_sales = (
            Order.objects.filter(
                created_at__range=(start_date - (end_date - start_date), start_date)
            ).aggregate(total=Sum("total_cost"))["total"]
            or 0
        )
        current_period_sales = (
            Order.objects.filter(created_at__range=(start_date, end_date)).aggregate(
                total=Sum("total_cost")
            )["total"]
            or 0
        )

        return (
            ((current_period_sales - previous_period_sales) / previous_period_sales)
            * 100
            if previous_period_sales != 0
            else 0
        )

    @staticmethod
    def average_order_value():
        """
        Calculate average order value.

        Returns:
            float: The average order value.
        """
        total_revenue = Order.objects.aggregate(total=Sum("total_cost"))["total"] or 0
        total_orders = Order.objects.count()

        return total_revenue / total_orders if total_orders != 0 else 0
