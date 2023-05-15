import hashlib
from django.db import models
from django.core.validators import FileExtensionValidator


class Media(models.Model):
    """
    Media model to represent images, videos, or gifs associated with a product variant.

    Represents media items, such as images, videos, or gifs, that are associated with a product variant.
    Typically, there will be 4 or more media items for every product variant when available.
    """

    id = models.AutoField(primary_key=True)
    """The unique identifier of the media item."""

    name = models.CharField(max_length=32, unique=True, editable=True, null=False)
    """The name of the media item."""

    hash = models.CharField(max_length=64, editable=True, default=" ")
    """The signature hash of the media item."""

    media_type = models.CharField(max_length=4)
    """The type of the media item (e.g., url, png, jpg, gif)."""

    image = models.ImageField(
        upload_to="products/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "gif"],
                message="File format not supported.",
            )
        ],
        null=True,
    )
    """The image file of the media item."""

    def __str__(self):
        """
        Return the name of the Media instance as its default string representation.

        Returns the name of the media item with its identifier and media type.
        """
        return f"{self.name}-{self.id}.{self.media_type}"

    def save(self, *args, **kwargs):
        """
        Save the Media instance.

        Generate the signature hash of the media item before saving it.
        """
        self.generate_image_hash()
        super(Media, self).save(*args, **kwargs)

    def generate_image_hash(self):
        """
        Generate the signature hash of the media item.

        Calculate the SHA256 hash of the image file content and store it in the `hash` field.
        """
        file_content = self.image.read()
        self.hash = hashlib.sha256(file_content).hexdigest()
