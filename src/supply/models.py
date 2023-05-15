from django.db import models
import uuid


class Info(models.Model):
    """
    Model to represent the supply of a specific product.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    product_variant = models.ForeignKey(
        "product.Variant", on_delete=models.CASCADE, related_name="supplies"
    )
    supplier = models.ForeignKey(
        "supply.Supplier",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="supply_info",
    )
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.PositiveIntegerField(null=False, default=1)

    # Valid indentification of the units are not present, they are currently simulated
    # (project not used for production atm), field is present on product.Unit.serial

    def __str__(self):
        return f"{self.product_variant.name} - Total cost: {self.total_cost} from {self.supplier.name}"

    @property
    def total_cost(self):
        return self.cost_per_unit * self.quantity

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        from product.models import Unit

        for _ in range(self.quantity):
            Unit.objects.create(variant_id=self.product_variant, supply=self)


class Supplier(models.Model):
    """
    Model to represent a supplier.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    # Add address field

    def __str__(self):
        return self.name
