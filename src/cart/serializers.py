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

    def validate(self, data):
        client = self.context['request'].user
        quantity = data.get('quantity')
        if client.is_enterprise and quantity > 100:
            raise serializers.ValidationError("Enterprise users can order up to 100 units at a time.")
        elif not client.is_enterprise and quantity > 10:
            raise serializers.ValidationError("Non-enterprise users can order up to 10 units at a time.")
        return data


class CartInfoSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = ["id", "user", "created_at", "updated_at", "items"]
