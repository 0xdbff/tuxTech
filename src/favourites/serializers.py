from rest_framework import serializers
from .models import Info, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "cart", "variant", "quantity", "created_at", "updated_at"]

    def create(self, validated_data):
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
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = ["id", "user", "created_at", "updated_at", "items"]
