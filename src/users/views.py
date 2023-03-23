from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views import View
from .models import Client
from .serializers import ClientSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

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


# Create your views here.
