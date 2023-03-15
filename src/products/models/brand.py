""" Product models"""
from django.db import models
import uuid


class Brand(models.Model):
    """
    Brand model to represent different product manufacturers.
    Examples include AMD, Intel, and NVIDIA.
    """

    name = models.CharField(max_length=32)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        """Instance name"""
        return self.name
