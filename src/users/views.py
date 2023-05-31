from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from .models import Client, Address, CreditCard
from .serializers import (
    ClientSerializer,
    UserLoginSerializer,
    CreditCardSerializer,
    AddressSerializer,
    CountrySerializer,
    CitySerializer,
)
from cities.models import Country, City
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    """
    A view for user login.
    """

    def post(self, request):
        """
        Handle user login.
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class ClientRegistrationView(generics.CreateAPIView):
    """
    A view for registering new clients.
    """

    serializer_class = ClientSerializer


class ClientView(generics.RetrieveUpdateAPIView):
    """
    A view for retrieving and updating client information.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = "id"


class AddressCreateView(generics.CreateAPIView):
    """
    A view for creating new addresses.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressView(generics.RetrieveUpdateAPIView):
    """
    A view for retrieving and updating addresses.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "id"


class AddressDeleteView(generics.DestroyAPIView):
    """
    A view for deleting addresses.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "id"


class ListCountriesView(generics.ListAPIView):
    """
    A view for listing countries.
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ListCitiesView(generics.ListAPIView):
    """
    A view for listing cities.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned cities to a given country,
        by filtering against a `country` query parameter in the URL.
        """
        queryset = City.objects.all()
        country_id = self.request.GET.get("country", None)
        if country_id is not None:
            country = get_object_or_404(Country, id=country_id)
            queryset = queryset.filter(country=country)
        return queryset


class CreditCardCreateView(generics.CreateAPIView):
    """
    A view for creating new credit cards.
    """

    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer


class CreditCardView(generics.RetrieveUpdateAPIView):
    """
    A view for retrieving and updating credit card information.
    """

    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    lookup_field = "id"


class CreditDeleteView(generics.DestroyAPIView):
    """
    A view for deleting credit cards.
    """

    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    lookup_field = "id"
