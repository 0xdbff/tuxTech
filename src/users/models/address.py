from django.core.validators import RegexValidator
from django.db import models
from cities.models import City, Country


class Address(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
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
                r"^\d{5}(-\d{4})?$",
                message="Postal code must be in the format '12345' or '12345-6789'.",
            )
        ],
    )

    class Meta:
        unique_together = (
            "client",
            "country",
            "city",
            "street",
            "house_number",
            "apartment_number",
            "postal_code",
        )

    def __str__(self):
        return f"{self.street} {self.house_number}\n{self.city}, {self.postal_code}, {self.country}"
