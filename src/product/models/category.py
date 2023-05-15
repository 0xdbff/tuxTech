from django.db import models
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    """
    Category model to represent different product categories.

    Represents a category, such as Computers, Servers, or Mobile Devices.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=True)
    """The name of the category."""

    description = models.TextField()
    """The description of the category."""

    image = models.ImageField(
        upload_to="categories/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["png", "svg"],
                message="File format not supported.",
            )
        ],
        null=False,
    )
    """The image file of the category."""

    _sku_prefix = models.CharField(max_length=2, editable=False, null=False)
    """The first prefix for the stock keeping unit (SKU) representing the category."""

    def __str__(self):
        """
        Return the name of the Category instance as its default string representation.

        Returns the name of the category.
        """
        return self.name
