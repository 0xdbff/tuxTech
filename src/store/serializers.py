from rest_framework import serializers
from .models import PromotionApplication

class PromotionApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for PromotionApplication model.
    It includes all the fields by default.
    """
    class Meta:
        model = PromotionApplication
        fields = '__all__'

