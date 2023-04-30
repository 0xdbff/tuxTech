from rest_framework import serializers
from .models import Client, TuxTechUser
from django.contrib.auth.models import Permission


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        print("F1")
        user = TuxTechUser.objects.filter(email=data["email"]).first()
        print(user)
        if user and user.check_password(data["password"]):
            print(data)
            return user
        print(data)
        raise serializers.ValidationError("Invalid email or password")


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
