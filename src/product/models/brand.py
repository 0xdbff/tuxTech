from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import hashlib
from django.core.files.storage import default_storage


class Brand(models.Model):
    """
    Brand model to represent different product manufacturers.

    Represents a brand, such as AMD, Intel, or NVIDIA.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=True)
    """The name of the brand."""

    logo_hash = models.CharField(max_length=64, editable=True, default=" ", null=False)
    """The signature hash of the brand's logo."""

    logo_type = models.CharField(max_length=4)
    """The image type of the brand's logo, such as PNG or SVG."""

    logo = models.ImageField(
        upload_to="logos/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["png", "svg"],
                message="File format not supported.",
            )
        ],
        null=False,
    )
    """The image file of the brand's logo."""

    date_added = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """
        Save method overridden to generate the image hash and save the Brand object.

        This method generates the SHA-256 hash of the brand's logo image content
        and assigns it to the logo_hash field before saving the object.
        """
        self.generate_image_hash()
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        """
        Return the name of the Brand instance as its default string representation.

        Returns the name of the brand.
        """
        self.generate_image_hash()
        return self.name

    def generate_image_hash(self):
        """
        Generate the SHA-256 hash of the brand's logo image.

        This method reads the content of the logo image file and computes the
        SHA-256 hash of the content. The resulting hash is assigned to the
        logo_hash field.
        """
        file_content = self.logo.read()
        self.logo_hash = hashlib.sha256(file_content).hexdigest()
