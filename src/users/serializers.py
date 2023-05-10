from rest_framework import serializers
from .models import Client, TuxTechUser
from django.contrib.auth.models import Permission
from cities.models import Country, City
from .models import Address
from .models import TuxTechUser


class TuxTechUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuxTechUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "gender",
            "username",
            "email",
            "date_of_birth",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "username": {"required": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = TuxTechUser.objects.create_user(**validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = TuxTechUser.objects.filter(email=data["email"]).first()
        if user and user.check_password(data["password"]):
            print(data)
            return user
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

        user = TuxTechUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        instance = self.Meta.model(user=user, **validated_data)
        instance.save()

        instance.user_permissions.set(Permission.objects.none())
        return instance


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "client",
            "country",
            "city",
            "street",
            "house_number",
            "apartment_number",
            "postal_code",
        ]
