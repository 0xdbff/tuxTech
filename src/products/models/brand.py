""" Product models"""
from django.db import models


class Brand(models.Model):
    """
    Brand model to represent different product manufacturers.
    Examples include AMD, Intel, and NVIDIA.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=False)
    logo = models.ForeignKey(
        "Media", on_delete=models.CASCADE, related_name="logo_image"
    )

    def __str__(self):
        """Instance name"""
        return self.name
