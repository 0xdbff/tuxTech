""" """
from django.db import models


class Type(models.Model):
    """
    Category model to represent different product categories.
    Examples include Computers, Servers, and Mobile Devices.
    """

    name = models.CharField(max_length=64, primary_key=True, editable=True)
    description = models.TextField()
    type = models.ForeignKey(
        "SubCategory",
        on_delete=models.CASCADE,
        related_name="type",
        null=False,
        editable=True,
    )
    _sku_prefix = models.CharField(max_length=2, editable=False, null=False)
    """Stock's keeping unit first prefix (Product Type)"""

    def __str__(self):
        """ """
        return self.name
