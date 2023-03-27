""" """
from django.db import models


class SubCategory(models.Model):
    """
    Category model to represent different product categories.
    Examples include Computers, Servers, and Mobile Devices.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=True)
    description = models.TextField()
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="sub_category",
        null=False,
        editable=True,
    )

    def __str__(self):
        """ """
        return self.name
