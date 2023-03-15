""" Product models"""
from django.db import models
import uuid


class Unit(models.Model):
    """
    Product model to represent individual instances of a specific product.
    """

    type = models.ForeignKey(
        "Info",
        on_delete=models.CASCADE,
        related_name="instances",
        null=False,
        editable=False,
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        """Instance name"""
        return f"{self.type.name} - ({self.id})"
