from django.test import TestCase
from cities.models import City, Country
from users.models import Client, Address


class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client.objects.create(
            email="client@test.com",
            username="client",
            password="testpassword",
            is_staff=False,
            is_superuser=False,
        )

        cls.address = Address.objects.create(
            client=cls.client,
            # country=cls.country,
            # city=cls.city,
            street="Test Street",
            house_number="1A",
        )

        cls.client.default_invoice_address = cls.address
        cls.client.default_shipping_address = cls.address
        cls.client.save()

    # def test_default_invoice_address(self):
    #     """
    #     Test that the default invoice address is set when an address is created.
    #     """
    #     self.assertEqual(self.client.default_invoice_address, self.address)
    #
    # def test_default_shipping_address(self):
    #     """
    #     Test that the default shipping address is set when an address is created.
    #     """
    #     self.assertEqual(self.client.default_shipping_address, self.address)
