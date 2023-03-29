""" Product models"""
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

import hashlib
from django.core.files.storage import default_storage


class Brand(models.Model):
    """
    Brand model to represent different product manufacturers.
    Examples include AMD, Intel, and NVIDIA.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=True)
    """Brand name"""
    logo_hash = models.CharField(max_length=64, editable=True, default=" ", null=False)
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

    def save(self, *args, **kwargs):
        self.generate_image_hash()
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        """Instance name"""
        self.generate_image_hash()
        return self.name

    def generate_image_hash(self):
        file_content = self.logo.read()
        self.logo_hash = hashlib.sha256(file_content).hexdigest()
