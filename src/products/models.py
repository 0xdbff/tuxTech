""" Product models"""
from django.db import models
import uuid


class Specification(models.Model):
    """
    Specification model to store individual product specifications.
    Each specification consists of a name and a value (e.g., color: red).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    value = models.TextField(null=False)
    # SET comparison methods

    def __str__(self):
        """Instance name"""
        return self.name


class Categorie(models.Model):
    """
    Category model to represent different product categories.
    Examples include Computers, Servers, and Mobile Devices.
    """

    name = models.CharField(max_length=32)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        """Instance name"""
        return self.name


class Brand(models.Model):
    """
    Brand model to represent different product manufacturers.
    Examples include AMD, Intel, and NVIDIA.
    """

    name = models.CharField(max_length=32)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        """Instance name"""
        return self.name


class ProductInfo(models.Model):
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
    specifications = models.ManyToManyField(Specification, null=False)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        """Get the product type and reference"""
        return f"{self.name} - ({self.sku})"

    @property
    def stock(self):
        return Product.objects.filter(type=self).count()

    @property
    def stock_value(self):
        return self.stock * self.price


class Product(models.Model):
    """
    Product model to represent individual instances of a specific product.
    """

    type = models.ForeignKey(
        ProductInfo,
        on_delete=models.CASCADE,
        related_name="instances",
        null=False,
        editable=False,
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        """Instance name"""
        return f"{self.type.name} - ({self.id})"
