from django.test import TestCase
from .models import CreditCard, Client, Address
from .validators import validate_card_number
from django.core.exceptions import ValidationError
from cities.models import City, Country
from django.contrib.gis.geos import Point


class CreditCardTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create_user(
            email="test@example.com",
            password="testpassword",
            username="testuser",
        )

    def test_card_type_detection(self):
        visa_card = CreditCard(
            client=self.client,
            cardholder_name="card holder",
            card_number="4111111111111111",
            expiry_month=12,
            expiry_year=2025,
            cvv="123",
        )
        visa_card.save()
        self.assertEqual(visa_card.card_type, "VISA")

        mastercard_card = CreditCard(
            client=self.client,
            cardholder_name="card holder",
            card_number="5555555555554444",
            expiry_month=1,
            expiry_year=2027,
            cvv="321",
        )
        mastercard_card.save()
        self.assertEqual(mastercard_card.card_type, "MASTERCARD")

        unknown_card = CreditCard(
            client=self.client,
            cardholder_name="Unknown User",
            card_number="1234567812345678",
            expiry_month=6,
            expiry_year=2026,
            cvv="456",
        )
        unknown_card.save()
        self.assertEqual(unknown_card.card_type, "UNKNOWN")

    def test_card_number_validation(self):
        valid_card_number = "4111111111111111"
        invalid_card_number = "4111111111111112"

        self.assertIsNone(validate_card_number(valid_card_number))

        with self.assertRaises(ValidationError):
            validate_card_number(invalid_card_number)


class AddressModelTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(
            nif="123456789",
            email="test@example.com",
            username="testuser",
            password="testpassword",
        )
        self.country_obj = Country.objects.create(
            name="Test Country",
            code="TC",
            code3="TCY",
            population=0,
            area=0,
            currency="USD",
            currency_name="US Dollar",
            currency_symbol="$",
            language_codes="en",
            phone="1",
            tld="tc",
            postal_code_format="",
            postal_code_regex="",
        )
        self.city_obj = City.objects.create(
            name="Test City",
            country=self.country_obj,
            population=0,
            location=Point(0, 0),
        )


    def test_address_creation(self):
        address = Address.objects.create(
            client=self.client_obj,
            country=self.country_obj,
            city=self.city_obj,
            street="Test Street",
            house_number="123",
            apartment_number="4A",
            postal_code="12345",
        )

        self.assertEqual(
            str(address), "Test Street 123, Test City, 12345, Test Country"
        )

    def test_address_validators(self):
        # Test with an invalid house number
        with self.assertRaises(ValidationError):
            address = Address(
                client=self.client_obj,
                country=self.country_obj,
                city=self.city_obj,
                street="Test Street",
                house_number="123@",
                apartment_number="4A",
                postal_code="12345",
            )
            address.full_clean()

        # Test with an invalid postal code
        with self.assertRaises(ValidationError):
            address = Address(
                client=self.client_obj,
                country=self.country_obj,
                city=self.city_obj,
                street="Test Street",
                house_number="123",
                apartment_number="4A",
                postal_code="123456",
            )
            address.full_clean()
