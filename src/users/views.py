from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Client
from .serializers import ClientSerializer
from .serializers import UserLoginSerializer
from .models import Address
from .serializers import AddressSerializer, CountrySerializer, CitySerializer
from cities.models import Country, City
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request):
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


class ClientJsonView(View):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(pk=kwargs["client_id"])
            serializer = ClientSerializer(client)
            return JsonResponse(serializer.data)
        except Client.DoesNotExist:
            return JsonResponse({"error": "Client not found"}, status=404)


class ClientRegistrationView(generics.CreateAPIView):
    serializer_class = ClientSerializer


class AddAddressView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class ListCountriesView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ListCitiesView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]

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
