from rest_framework import serializers
from django.contrib.auth.models import Permission
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("email", "username", "nif", "password", "receive_news")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "username": {"required": False},
            "nif": {"required": False},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        if password is None:
            return
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)

        instance.user_permissions.set(Permission.objects.none())
        instance.last_login = None

        instance.save()
        return instance
