from django.db import models


class Favourites(models.Model):
    user = models.OneToOneField("Client", on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of user {self.user.username}"


class FavouritesItem(models.Model):
    cart = models.ForeignKey(Favourites, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey("Variant", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return (
            f"(cart {self.cart.user.id} : item - {self.variant.sku}) x {self.quantity}"
        )
