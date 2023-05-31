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
    )
    order = models.ForeignKey(
        "order.Order",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="units",
    )
    supply = models.ForeignKey(
        "supply.info",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="supply_units",
    )

    serial = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        """Instance name"""
        return f"{self.variant_id.name} - ({self.serial})"
