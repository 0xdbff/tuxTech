""" Product models"""
from django.db import models
import uuid


class Unit(models.Model):
    """
    Product model to represent individual instances of a specific product.
    """

    variant_id = models.ForeignKey(
        "Variant",
        on_delete=models.CASCADE,
        related_name="instances",
        null=False,
        editable=False,
    )
    serial = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        """Instance name"""
        return f"{self.variant_id.name} - ({self.serial})"
