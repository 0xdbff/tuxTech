from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import Admin, Client


class ClientModelBackend(BaseBackend):
    def authenticate(self, input=None, password=None, **kwargs):
        try:
            user = Client.objects.get(email=input)
        except Client.DoesNotExist:
            try:
                user = Client.objects.get(username=input)
            except Client.DoesNotExist:
                return None

        if password and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None


class AdminModelBackend(BaseBackend):
    def authenticate(self, request, input=None, password=None, **kwargs):
        email_or_username = request.POST.get("email") or request.POST.get("username")
        print(f"Input email/username: {email_or_username}")
        try:
            user = Admin.objects.get(email=email_or_username)
        except Admin.DoesNotExist:
            try:
                user = Admin.objects.get(username=email_or_username)
                print("Authentication successful")
            except Admin.DoesNotExist:
                print("Admin not found")
                return None

        if password and user.check_password(password):
            print("Password verified")
            return user
        return None

    def get_user(self, user_id):
        try:
            return Admin.objects.get(pk=user_id)
        except Admin.DoesNotExist:
            print("Admin not found in get_user")
            return None
