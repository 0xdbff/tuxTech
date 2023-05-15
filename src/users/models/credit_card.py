from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date
from ..validators import validate_card_number
import uuid


class CreditCard(models.Model):
    """
    Model representing a credit card associated with a client.
    """

    CARD_TYPES = (
        ("VISA", "Visa"),
        ("MASTERCARD", "Mastercard"),
        ("UNKNOWN", "Unknown"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="credit_cards"
    )
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16, validators=[validate_card_number])
    card_type = models.CharField(max_length=10, choices=CARD_TYPES, default="UNKNOWN")
    expiry_month = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    expiry_year = models.PositiveIntegerField(
        validators=[MinValueValidator(date.today().year)]
    )
    cvv = models.CharField(max_length=4)

    def __str__(self):
        """
        Returns a string representation of the credit card.
        :return: The string representation of the credit card.
        :rtype: str
        """
        return f"{self.cardholder_name}: **** **** **** {self.card_number[-4:]}"

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set the card type based on the card number.
        :param args: Additional arguments.
        :param kwargs: Additional keyword arguments.
        """
        self.card_type = self.get_card_type()
        super(CreditCard, self).save(*args, **kwargs)

    def get_card_type(self):
        """
        Determines and returns the card type based on the card number.
        :return: The card type.
        :rtype: str
        """
        if self.card_number.startswith("4"):
            return "VISA"
        elif self.card_number.startswith(("51", "52", "53", "54", "55")):
            return "MASTERCARD"
        else:
            return "UNKNOWN"
