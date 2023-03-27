""" Product models"""
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class Brand(models.Model):
    """
    Brand model to represent different product manufacturers.
    Examples include AMD, Intel, and NVIDIA.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=True)
    """Brand name"""
    logo_hash = models.CharField(max_length=64, editable=True, default=" ")
    """Logo signature hash"""
    logo_type = models.CharField(max_length=4)
    """Logo image type -> png, svg"""

    logo = models.ImageField(
        upload_to="logos/",  # !TODO change to /var/TuxTech/media
        validators=[
            FileExtensionValidator(
                allowed_extensions=["png", "svg"],
                message="File format not supported.",
            )
        ],
        null=False,
    )
    """Logo image"""

    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Instance name"""
        return self.name

    # !TODO gen hash
