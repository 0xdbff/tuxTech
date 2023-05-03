from django.contrib.auth import get_user_model
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views import View
from .models import Client
from .backends import CustomModelBackend


from .serializers import ClientSerializer


# class LoginView(APIView):
#     def post(self, request):
#         input = request.data.get("username")
#         password = request.data.get("password")
#         backend = CustomModelBackend()
#         user = backend.authenticate(input=input, request=request, password=password)
#
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response(
#                 {
#                     "refresh": str(refresh),
#                     "access": str(refresh.access_token),
#                 }
#             )
#         else:
#             return Response(
#                 {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
#             )


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

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


class AdminLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        input = request.data.get("username")
        password = request.data.get("password")

        print("Received input:", input)  # Debug print
        print("Received password:", password)  # Debug print

        backend = backend = CustomModelBackend()
        user = backend.authenticate(
            request=request, input=input, password=password, admin_only=True
        )

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
