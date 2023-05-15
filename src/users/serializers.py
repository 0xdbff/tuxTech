from rest_framework import serializers
from django.contrib.auth.models import Permission
from cities.models import Country, City
from .models import TuxTechUser, CreditCard, Address, Client
from django.core.mail import send_mail


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """
        Validate user login data.
        :param dict data: user login data
        :return: validated user
        :rtype: TuxTechUser
        :raises serializers.ValidationError: if email or password is invalid
        """
        user = TuxTechUser.objects.filter(email=data["email"]).first()
        if user and user.check_password(data["password"]):
            return user
        raise serializers.ValidationError("Invalid email or password")


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for address model.
    """

    class Meta:
        model = Address
        fields = "__all__"

    def get_fields(self):
        """
        Get the serializer fields and customize queryset for city and country fields.
        :return: serializer fields
        :rtype: dict
        """
        fields = super(AddressSerializer, self).get_fields()
        fields["city"].queryset = City.objects.filter(country__name="Portugal")
        fields["country"].queryset = Country.objects.filter(name="Portugal")
        return fields

    def validate(self, data):
        """
        Validate address data.
        :param dict data: address data
        :return: validated data
        :rtype: dict
        :raises serializers.ValidationError: if the city does not belong to the selected country
        """
        city = data.get("city")
        country = data.get("country")
        if city and country and city.country != country:
            raise serializers.ValidationError(
                "The city does not belong to the selected country."
            )
        return data


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for client model.
    """

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
        """
        Create a new client.
        :param dict validated_data: validated client data
        :return: created client
        :rtype: Client
        :raises serializers.ValidationError: if password is missing
        """
        password = validated_data.pop("password", None)
        if password is None:
            raise serializers.ValidationError({"password": "This field is required."})
        client = Client.objects.create_user(**validated_data, password=password)

        send_mail(
            "Welcome To TuxTech",
            f"We are happy to report that {client.first_name} {client.last_name}"
            + "is now an official TuxTech Client!\n\nThe TuxTeach team,\nbest regards!",
            "home@gldb.dev",
            [f"{client.email}"],
            fail_silently=False,
        )

        return client

    def update(self, instance, validated_data):
        """
        Update an existing client.
        :param Client instance: existing client instance
        :param dict validated_data: validated client data
        :return: updated client
        :rtype: Client
        """
        password = validated_data.pop("password", None)
        client = super().update(instance, validated_data)
        if password:
            client.set_password(password)
            client.save()
        return client


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for country model.
    """

    class Meta:
        model = Country
        fields = ["id", "name"]


class CitySerializer(serializers.ModelSerializer):
    """
    Serializer for city model.
    """

    class Meta:
        model = City
        fields = ["id", "name"]


class CreditCardSerializer(serializers.ModelSerializer):
    """
    Serializer for credit card model.
    """

    class Meta:
        model = CreditCard
        fields = "__all__"
        extra_kwargs = {
            "cvv": {
                "write_only": True
            },  # Ensure cvv is never exposed in any API response
        }
