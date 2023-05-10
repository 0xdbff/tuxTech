from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import OrderedItem, Order, OrderStatus
from product.models import Variant
from users.models import Address

User = get_user_model()


class OrderedItemTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testemail@example.com', password='testpassword'
        )
        self.address = Address.objects.create(
            user=self.user, street_address="123 Street", city="City", zip_code="12345"
        )
        self.order = Order.objects.create(
            customer=self.user,
            shipping_address=self.address,
            billing_address=self.address,
        )
        self.variant = Variant.objects.create(name="Test Variant", price=100.0)
        self.ordered_item = OrderedItem.objects.create(
            order=self.order, product_variant=self.variant, quantity=1
        )

    def test_ordered_item_creation(self):
        self.assertIsInstance(self.ordered_item, OrderedItem)
        self.assertEqual(self.ordered_item.order.customer.username, "testuser")

    def test_ordered_item_total_price(self):
        self.assertEqual(self.ordered_item.total_price, 100.0)


class OrderTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testemail@example.com', password='testpassword'
        )
        self.address = Address.objects.create(
            user=self.user, street_address="123 Street", city="City", zip_code="12345"
        )
        self.order = Order.objects.create(
            customer=self.user,
            shipping_address=self.address,
            billing_address=self.address,
        )

    def test_order_creation(self):
        self.assertIsInstance(self.order, Order)
        self.assertEqual(self.order.customer.username, "testuser")

    def test_order_status(self):
        self.assertEqual(self.order.status, OrderStatus.CREATED.value)

    def test_confirm_payment(self):
        self.order.confirm_payment()
        self.assertEqual(self.order.status, OrderStatus.PAYMENT_CONFIRMED.value)
