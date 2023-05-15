from rest_framework import serializers
from .models import Support


class SupportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Support model.

    This serializer converts the Support model instance into a format that can
    be easily rendered into JSON, XML, or other content types.
    It also provides deserialization, validating incoming data.
    """

    class Meta:
        model = Support
        fields = "__all__"
