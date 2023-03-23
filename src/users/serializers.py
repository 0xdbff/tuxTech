from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("email", "username", "nif", "password", "receive_news")
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"required": False},
            "nif": {"required": False},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
