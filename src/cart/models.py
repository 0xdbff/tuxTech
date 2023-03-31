from django.db import models
from django.conf import settings


class Info(models.Model):
    user = models.OneToOneField(
        "users.client",
        on_delete=models.CASCADE,
        related_name="cart_info",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of user {self.user.username}"


class Item(models.Model):
    cart = models.ForeignKey(Info, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(
        "product.variant", on_delete=models.CASCADE, related_name="cart_item"
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.variant.name} ({self.variant.sku}) x {self.quantity} in cart {self.cart.id}"
