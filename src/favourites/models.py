from django.db import models
import uuid


class Info(models.Model):
    """
    Model to store information about a user's favourites.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4().hex)
    """Unique identifier for the Info instance."""
    user = models.OneToOneField(
        "users.client",
        on_delete=models.CASCADE,
        related_name="favourites_info",
    )
    """One-to-One relationship with the Client model, representing the user."""
    created_at = models.DateTimeField(auto_now_add=True)
    """Date and time when the Info instance was created."""
    updated_at = models.DateTimeField(auto_now=True)
    """Date and time when the Info instance was last updated."""

    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the user's favourites reference.

        When an Info instance is saved, it checks if the user's favourites field is not set.
        If not set, it sets the user's favourites field to the current Info instance and saves the user.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        super().save(*args, **kwargs)

        if not self.user.favourites:
            self.user.favourites = self
            self.user.save(update_fields=["favourites"])

    def __str__(self):
        """
        Returns a string representation of the Info instance.

        Returns:
            str: A string representation of the Info instance.
        """
        return f"Cart of user {self.user.username}"


class Item(models.Model):
    """
    Model to represent an item in a user's favourites.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    """Unique identifier for the Item instance."""
    cart = models.ForeignKey(Info, on_delete=models.CASCADE, related_name="items")
    """Foreign key to the Info model, representing the user's favourites."""
    variant = models.ForeignKey(
        "product.variant",
        on_delete=models.CASCADE,
        related_name="favourites_item",
    )
    """Foreign key to the Variant model, representing the item's product variant."""
    created_at = models.DateTimeField(auto_now_add=True)
    """Date and time when the Item instance was created."""
    updated_at = models.DateTimeField(auto_now=True)
    """Date and time when the Item instance was last updated."""

    class Meta:
        unique_together = ("cart", "variant")
        """Defines a unique constraint for the combination of cart and variant fields."""

    def __str__(self):
        """
        Returns a string representation of the Item instance.

        Returns:
            str: A string representation of the Item instance.
        """
        return (
            f"(cart {self.cart.user.id} : item - {self.variant.sku}) x {self.quantity}"
        )
