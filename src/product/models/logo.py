""" Product models"""
import hashlib
from django.db import models
from django.core.validators import FileExtensionValidator


class Logo(models.Model):
    """ """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True, editable=True, null=False)
    hash = models.CharField(max_length=64, editable=True, default=" ")
    """Signature hash"""
    media_type = models.CharField(max_length=4)
    """Media type -> png, svg"""

    image = models.ImageField(
        upload_to="logos/",  # !TODO change to /var/TuxTech/media
        validators=[
            FileExtensionValidator(
                allowed_extensions=["png", "svg"],
                message="File format not supported.",
            )
        ],
        null=False,
    )

    def __str__(self):
        """Instance name"""
        return f"logo@{self.name}.{self.media_type}"
