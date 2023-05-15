from rest_framework import serializers
from .models import Info, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer for the Supplier model.

    Serializes the Supplier model fields.
    """

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplySerializer(serializers.ModelSerializer):
    """
    Serializer for the Info model.

    Serializes the Info model fields.
    """

    class Meta:
        model = Info
        fields = "__all__"
