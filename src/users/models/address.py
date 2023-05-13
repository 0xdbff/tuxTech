from django.core.validators import RegexValidator
from django.db import models
from cities.models import City, Country
import uuid


def generate_uuid():
    return uuid.uuid4


class Address(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=generate_uuid())
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    street = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    house_number = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                r"^\d+[a-zA-Z\s\-]*$",
                message="House number can only contain digits, letters, spaces, and hyphens.",
            )
        ],
    )
    apartment_number = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                r"^[a-zA-Z0-9\s\-]*$",
                message="Postal code can only contain digits, letters, spaces, and hyphens.",
            )
        ],
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.client.default_invoice_address:
            self.client.default_invoice_address = self
            self.client.save(update_fields=["default_invoice_address"])

        if not self.client.default_shipping_address:
            self.client.default_shipping_address = self
            self.client.save(update_fields=["default_shipping_address"])

    def __str__(self):
        return f"{self.street} {self.house_number}\n{self.city}, {self.postal_code}, {self.country}"
