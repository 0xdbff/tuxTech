""" Product models"""
from django.db import models
from django.utils import timezone
from .category import Category
from .brand import Brand
from .specification import Specification
from .variant import Variant


class BaseInfo(models.Model):
    """
    Product.baseInfo model to store general information about a product,
    including its name, description, max an min price, and associated specifications.
    Because we had to address multiple options for a product ex(ssd size), variations
    were created, so there is at the bare minimmum a product.variation for every
    product.baseInfo.
    """

    ean = models.CharField(max_length=14, primary_key=True, editable=False)
    name = models.TextField(null=False)
    description = models.TextField(null=False)

    # !TODO setup autoupdate for this fields, make this properties.
    price_min = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    price_max = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="base_info"
    )
    """ A reference to this product's category."""
    subCategory = models.ForeignKey(
        "SubCategory", on_delete=models.CASCADE, related_name="base_info"
    )
    """ A reference to this product's sub-category."""
    ptype = models.ForeignKey(
        "Type", on_delete=models.CASCADE, related_name="base_info"
    )
    """ A reference to this product's type."""
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="product_baseInfo",
        editable=False,
        null=False,
    )
    """ A reference to this product's brand."""
    specifications = models.ManyToManyField(Specification)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Get the product's type and reference as default instance name"""
        return f"{self.name} - ({self.ean})"

    @property
    def variations(self):
        return Variant.objects.filter(info=self).count()

    @property
    def price(self):
        return (
            str(self.price_min)
            if self.price_min == self.price_max
            else f"{self.price_min} <-> {self.price_max}"
        )
