""" Product models"""
from django.db import models
from django.utils import timezone
from datetime import timedelta

from .variant import Variant
import uuid
from django.db.models import Min, Max


class BaseInfo(models.Model):
    """
    Product.baseInfo model to store general information about a product,
    including its name, description, max an min price, and associated specifications.
    Because we had to address multiple options for a product ex(ssd size), variations
    were created, so there is at the bare minimmum a product.variation for every
    product.baseInfo.
    """

    name = models.TextField(null=False)
    ref = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.TextField(null=False)

    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="base_info"
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
        "Brand",
        on_delete=models.CASCADE,
        related_name="product_baseInfo",
        null=False,
    )
    """ A reference to this product's brand."""
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Get the product's type and reference as default instance name"""
        return f"{self.name}-{self.ref})"

    @property
    def variations_count(self):
        """ """
        return Variant.objects.filter(info=self).count()

    @property
    def price_min(self):
        """ """
        min_price = Variant.objects.filter(info=self).aggregate(min_price=Min("price"))[
            "min_price"
        ]
        return min_price if min_price is not None else 0

    @property
    def price_max(self):
        """ """
        max_price = Variant.objects.filter(info=self).aggregate(max_price=Max("price"))[
            "max_price"
        ]
        return max_price if max_price is not None else 0

    @property
    def is_new(self):
        return (timezone.now() - self.date_added) <= timedelta(days=30)

    @property
    def price(self):
        """ """
        return (
            str(self.price_min)
            if self.price_min == self.price_max
            else f"{self.price_min} <-> {self.price_max}"
        )
