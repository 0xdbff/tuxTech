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
    name = models.CharField(max_length=32, unique=True, editable=False, null=False)
    hash = models.CharField(max_length=64, editable=True, default="")
    """Signature hash"""
    media_type = models.CharField(max_length=4)
    """Media type -> url, png, jpg, gif ..."""

    image = models.ImageField(
        upload_to="images/",
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
        return f"media@{self.name}.{self.media_type}"

    # def generate_hash(self):
    #     """
    #     Generate a 256-bit hash for the image and return it.
    #     """
    #     if self.image:
    #         with self.image.open("rb") as image_file:
    #             image_data = image_file.read()
    #         return hashlib.sha256(image_data).hexdigest()[:21]
    #     return ""

    # def save(self, *args, **kwargs):
    #     """
    #     Override the save method to update the hash field before saving.
    #     """
    #     if self.image:
    #         self.hash = self.generate_hash()
    #     super().save(*args, **kwargs)
