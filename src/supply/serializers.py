# supply/serializers.py
from rest_framework import serializers
from .models import Info, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"
