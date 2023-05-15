from django.db import models
import uuid


class Info(models.Model):
    """
    Model representing the cart information for a user.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(
        "users.client",
        on_delete=models.CASCADE,
        related_name="cart_info",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Saves the cart information.

        If the associated user does not have a cart, the cart information is assigned to the user.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super().save(*args, **kwargs)

        if not self.user.cart:
            self.user.cart = self
            self.user.save(update_fields=["cart"])

    def __str__(self):
        """
        Returns a string representation of the cart information.

        Returns:
            str: The string representation.
        """
        return f"Cart of user {self.user.username}"


class Item(models.Model):
    """
    Model representing an item in a cart.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    cart = models.ForeignKey(
        Info,
        on_delete=models.CASCADE,
        related_name="items",
    )
    variant = models.ForeignKey(
        "product.variant",
        on_delete=models.CASCADE,
        related_name="cart_item",
    )
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("cart", "variant")

    def __str__(self):
        """
        Returns a string representation of the item.

        Returns:
            str: The string representation.
        """
        return f"{self.variant.name} ({self.variant.sku}) x {self.quantity} in cart {self.cart.user.id}"
