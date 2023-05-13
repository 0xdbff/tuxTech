from rest_framework import serializers
from django.contrib.auth.models import Permission
from cities.models import Country, City
from .models import TuxTechUser, CreditCard, Address, Client


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = TuxTechUser.objects.filter(email=data["email"]).first()
        if user and user.check_password(data["password"]):
            print(data)
            return user
        raise serializers.ValidationError("Invalid email or password")


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def get_fields(self):
        fields = super(AddressSerializer, self).get_fields()
        fields["city"].queryset = City.objects.filter(country__name="Portugal")
        fields["country"].queryset = Country.objects.filter(name="Portugal")
        return fields

    def validate(self, data):
        city = data.get("city")
        country = data.get("country")
        if city and country and city.country != country:
            raise serializers.ValidationError(
                "The city does not belong to the selected country."
            )
        return data


class ClientSerializer(serializers.ModelSerializer):
    # default_invoice_address = AddressSerializer(read_only=True)
    # default_shipping_address = AddressSerializer(read_only=True)

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
            "default_invoice_address",
            "default_shipping_address",
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


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = "__all__"
        extra_kwargs = {
            "cvv": {
                "write_only": True
            },  # Ensure cvv is never exposed in any API response
        }
