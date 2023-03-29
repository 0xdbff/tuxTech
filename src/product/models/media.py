""" Product models"""
import hashlib
from django.db import models
from django.core.validators import FileExtensionValidator


class Media(models.Model):
    """
    Media model to represent images, videos, or gifs associated with a product variant.
    Typically, there will be 4 or more media items for every product variant when available.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True, editable=True, null=False)
    hash = models.CharField(max_length=64, editable=True, default=" ")
    """Signature hash"""
    media_type = models.CharField(max_length=4)
    """Media type -> url, png, jpg, gif ..."""

    image = models.ImageField(
        upload_to="products/",  # !TODO change to /var/TuxTech/media
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "gif"],
                message="File format not supported.",
            )
        ],
        null=True,
    )

    def __str__(self):
        """Instance name"""
        return f"{self.name}-{self.id}.{self.media_type}"

    def save(self, *args, **kwargs):
        self.generate_image_hash()
        super(Media, self).save(*args, **kwargs)

    def generate_image_hash(self):
        file_content = self.image.read()
        self.hash = hashlib.sha256(file_content).hexdigest()
