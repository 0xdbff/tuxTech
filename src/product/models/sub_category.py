from django.db import models


class SubCategory(models.Model):
    """
    SubCategory model to represent different sub-categories within a product category.

    Represents sub-categories within a product category, such as Computers, Servers, and Mobile Devices.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=True)
    """The name of the sub-category."""

    description = models.TextField()
    """The description of the sub-category."""

    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="sub_category",
        null=False,
        editable=True,
    )
    """A reference to the parent category of the sub-category."""

    _sku_prefix = models.CharField(max_length=2, editable=False, null=False)
    """The stock-keeping unit first prefix (Sub-Category)."""

    def __str__(self):
        """
        Return the name of the SubCategory instance as its default string representation.

        Returns the name of the sub-category.
        """
        return self.name
