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
    """ Product's name."""
    ref = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    """ Product's reference."""
    description = models.TextField(null=False)
    """ Product's description."""
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
        """
        Return the default instance name for the BaseInfo model.

        Returns the name and reference of the product.
        """
        return f"{self.name}-{self.ref})"

    @property
    def variations_count(self):
        """
        Retrieve the number of variations for the BaseInfo model.

        Returns the count of Variant objects associated with the BaseInfo model.
        """
        return Variant.objects.filter(info=self).count()

    @property
    def price_min(self):
        """
        Retrieve the minimum price for the BaseInfo model.

        Returns the minimum price among the Variant objects associated with the BaseInfo model.
        """
        min_price = Variant.objects.filter(info=self).aggregate(min_price=Min("price"))[
            "min_price"
        ]
        return min_price if min_price is not None else 0

    @property
    def price_max(self):
        """
        Retrieve the maximum price for the BaseInfo model.

        Returns the maximum price among the Variant objects associated with the BaseInfo model.
        """
        max_price = Variant.objects.filter(info=self).aggregate(max_price=Max("price"))[
            "max_price"
        ]
        return max_price if max_price is not None else 0

    @property
    def is_new(self):
        """
        Check if the BaseInfo model is new.

        Returns True if the product was added within the last 30 days, False otherwise.
        """
        return (timezone.now() - self.date_added) <= timedelta(days=30)

    @property
    def price(self):
        """
        Retrieve the price range for the BaseInfo model.

        Returns the price range as a string, either displaying the minimum price only if
        it's the same as the maximum price, or displaying both the minimum and maximum
        prices separated by a range indicator.
        """
        return (
            str(self.price_min)
            if self.price_min == self.price_max
            else f"{self.price_min} <-> {self.price_max}"
        )
