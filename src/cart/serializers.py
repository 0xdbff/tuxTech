from rest_framework import serializers
from .models import Info, Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the Item model.
    """

    class Meta:
        model = Item
        fields = ["id", "cart", "variant", "quantity", "created_at", "updated_at"]

    def create(self, validated_data):
        """
        Creates a new Item instance.

        If an item with the same cart and variant already exists, the quantity is incremented.
        Otherwise, a new item is created with the specified quantity.

        Args:
            validated_data (dict): Validated data for creating the item.

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

    def validate(self, data):
        """
        Validates the data for creating an item.

        Ensures that the quantity does not exceed the allowed limit based on the user's type.

        Args:
            data (dict): Data for creating the item.

        Returns:
            dict: Validated data.

        Raises:
            serializers.ValidationError: If the quantity exceeds the allowed limit.
        """
        client = self.context['request'].user
        quantity = data.get('quantity')
        if client.is_enterprise and quantity > 100:
            raise serializers.ValidationError("Enterprise users can order up to 100 units at a time.")
        elif not client.is_enterprise and quantity > 10:
            raise serializers.ValidationError("Non-enterprise users can order up to 10 units at a time.")
        return data


class CartInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Info model, representing a user's cart.
    """

    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = ["id", "user", "created_at", "updated_at", "items"]

