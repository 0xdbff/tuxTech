""" Product models"""
from django.db import models
from .categorie import Categorie
from .brand import Brand
from .specification import Specification
from .unit import Unit


class Info(models.Model):
    """
    ProductInfo model to store general information about a product,
    including its name, description, price, and associated specifications.
    """

    sku = models.CharField(max_length=32, primary_key=True, editable=False)
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    category = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name="product_info"
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="product_info",
        editable=False,
        null=False,
    )
    specifications = models.ManyToManyField(Specification)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        """Get the product type and reference"""
        return f"{self.name} - ({self.sku})"

    @property
    def stock(self):
        return Unit.objects.filter(type=self).count()

    @property
    def stock_value(self):
        return self.stock * self.price
