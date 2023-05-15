from rest_framework import serializers
from .models import Info, Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Item model.
    """

    class Meta:
        model = Item
        fields = ["id", "cart", "variant", "quantity", "created_at", "updated_at"]

    def create(self, validated_data):
        """
        Create method to handle the creation of an Item instance.

        If an Item with the same cart and variant already exists, the quantity
        is incremented. Otherwise, a new Item is created with the provided quantity.

        Returns:
            Item: The created or updated Item instance.
        """
        item, created = Item.objects.get_or_create(
            cart=validated_data["cart"],
            variant=validated_data["variant"],
            defaults={"quantity": validated_data["quantity"]},
        )

        if not created:
            item.quantity += validated_data["quantity"]
            item.save()

        return item


class FavouritesSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Info model, representing the user's favourites.
    """

    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = ["id", "user", "created_at", "updated_at", "items"]
