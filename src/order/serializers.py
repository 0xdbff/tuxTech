from rest_framework import serializers
from .models import Order, OrderedItem


class OrderedItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for the OrderedItem model.
    """

    class Meta:
        model = OrderedItem
        fields = ["id", "order", "product_variant", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Order model.
    """

    ordered_items = OrderedItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "customer",
            "created_at",
            "updated_at",
            "paid_at",
            "status",
            "shipping_address",
            "billing_address",
            "payment_info",
            "shipped_at",
            "include_nif",
            "ordered_items",
            "delivery_option",
        ]
