from rest_framework import serializers
from .models import Client, TuxTechUser
from django.contrib.auth.models import Permission
from cities.models import Country, City
from .models import Address
from .models import TuxTechUser


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
        fields = (
            "id",
            "first_name",
            "last_name",
            "gender",
            "username",
            "email",
            "date_of_birth",
            "password",
            "nif",
            "receive_news",
        )
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
            "email": {"required": True},
            "username": {"required": True},
            "nif": {"required": False},
            "gender": {"required": False},
            "date_of_birth": {"required": False},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        if password is None:
            raise serializers.ValidationError({"password": "This field is required."})
        client = Client.objects.create_user(**validated_data, password=password)
        return client

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        client = super().update(instance, validated_data)
        if password:
            client.set_password(password)
            client.save()
        return client


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name"]


# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = [
#             "id",
#             "client",
#             "country",
#             "city",
#             "street",
#             "house_number",
#             "apartment_number",
#             "postal_code",
#         ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
