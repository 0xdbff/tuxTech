from rest_framework import serializers
from .models import PromotionApplication
from .models import AdvertisementContract


class PromotionApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for PromotionApplication model.
    It includes all the fields by default.
    """

    class Meta:
        model = PromotionApplication
        fields = "__all__"


from rest_framework import serializers
from .models import AdvertisementContract


class AdvertisementContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementContract
        fields = [
            "start_date",
            "end_date",
            "advertisement_image",
            "ad_text",
            "priority",
        ]
