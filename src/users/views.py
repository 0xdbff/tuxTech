from django.contrib.auth import get_user_model
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views import View
from .models import Client
from .backends import ClientModelBackend, AdminModelBackend
from .serializers import ClientSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        input = request.data.get("input")
        password = request.data.get("password")
        backend = ClientModelBackend()
        user = backend.authenticate(input=input, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class AdminLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        input = request.data.get("username")
        password = request.data.get("password")
        backend = AdminModelBackend()
        user = backend.authenticate(input=input, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class ClientJsonView(View):
    def get(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(pk=kwargs["client_id"])
            serializer = ClientSerializer(client)
            return JsonResponse(serializer.data)
        except Client.DoesNotExist:
            return JsonResponse({"error": "Client not found"}, status=404)


class ClientRegistrationView(generics.CreateAPIView):
    serializer_class = ClientSerializer
