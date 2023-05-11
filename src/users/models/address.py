from django.core.validators import RegexValidator
from django.db import models
from cities.models import City, Country
import uuid


class Address(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4().hex)
    client = models.ForeignKey("users.TuxTechUser", on_delete=models.CASCADE)
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

    def __str__(self):
        return f"{self.street} {self.house_number}\n{self.city}, {self.postal_code}, {self.country}"
