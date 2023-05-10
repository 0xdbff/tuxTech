from django.db import models, transaction
from celery import shared_task

from django.db import IntegrityError
from django.utils import timezone

from datetime import timedelta
from enum import Enum

import uuid


class OrderStatus(Enum):
    CREATED = "Created"
    PAYMENT_PENDING = "Payment Pending"
    PAYMENT_CONFIRMED = "Payment Confirmed"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class OrderedItem(models.Model):
    order = models.ForeignKey(
        "order.Order", related_name="ordered_items", on_delete=models.CASCADE
    )
    product_variant = models.ForeignKey("product.Variant", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if self.pk:  # If this item already exists in the database
            old_self = OrderedItem.objects.get(pk=self.pk)
            self.product_variant.units.filter(
                order=old_self.order
            ).delete()  # Return the old units to stock

        available_units = self.product_variant.units.filter(order__isnull=True)
        if available_units.count() < self.quantity:
            raise IntegrityError("Not enough stock for this product variant")

        super().save(*args, **kwargs)

        for unit in available_units[: self.quantity]:
            unit.order = self.order
            unit.save()

    @property
    def total_price(self):
        return self.product_variant.price * self.quantity


class Order(models.Model):
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

    def confirm_payment(self):
        with transaction.atomic():
            self.status = OrderStatus.PAYMENT_CONFIRMED.value
            self.save()

    def ship(self):
        with transaction.atomic():
            if self.status != OrderStatus.PAYMENT_CONFIRMED.value:
                raise ValueError("Cannot ship an order that hasn't been paid for.")
            self.status = OrderStatus.SHIPPED.value
            self.save()

    def deliver(self):
        with transaction.atomic():
            if self.status != OrderStatus.SHIPPED.value:
                raise ValueError("Cannot deliver an order that hasn't been shipped.")
            self.status = OrderStatus.DELIVERED.value
            self.save()

    def cancel(self):
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
        # If the order has been shipped and it's been 24 hours, mark it as delivered
        if self.shipped_at and timezone.now() - self.shipped_at >= timedelta(hours=24):
            self.status = OrderStatus.DELIVERED.value
        # If all items are in stock, mark the order as shipped
        # elif all(
        #     item.product_variant.units.filter(order__isnull=True).count()
        #     >= item.quantity
        #     for item in self.ordered_items.all()
        # ):
        #     self.status = OrderStatus.SHIPPED.value
        #     self.shipped_at = timezone.now()
        elif all(
            models.OrderedItem.objects.filter(order=self)
            .product_variant.units.filter(order__isnull=True)
            .count()
            >= models.OrderedItem.objects.filter(order=self).quantity
        ):
            self.status = OrderStatus.SHIPPED.value
            self.shipped_at = timezone.now()
            # !TODO integrate with transportation servicies
            self.status = OrderStatus.DELIVERED.value
        # If payment information has been provided, mark the order as payment confirmed
        elif self.payment_info:
            self.status = OrderStatus.PAYMENT_CONFIRMED.value
            # Update paid_at timestamp if it hasn't been set
            if not self.paid_at:
                self.paid_at = timezone.now()

        super().save(*args, **kwargs)
