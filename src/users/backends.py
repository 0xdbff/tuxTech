from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import Admin

Client = get_user_model()

class ClientModelBackend(BaseBackend):
    """ """

    def authenticate(self, input=None, password=None):
        """ """
        try:
            user = Client.objects.get(email=input)
        except Client.DoesNotExist:
            try:
                user = Client.objects.get(username=input)
            except Client.DoesNotExist:
                return None

        try:
            if password:
                if user.check_password(raw_password=password):
                    return user
            return None
        except:
            return None

    def get_user(self, user_id):
        """ """
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None


class AdminModelBackend(BaseBackend):
    """ """

    def authenticate(self, input=None, password=None):
        """ """
        try:
            user = Admin.objects.get(email=input)
        except Admin.DoesNotExist:
            try:
                user = Admin.objects.get(username=input)
            except Admin.DoesNotExist:
                return None

        try:
            if password:
                if user.check_password(raw_password=password):
                    return user
            return None
        except:
            return None

    def get_user(self, user_id):
        try:
            return Admin.objects.get(pk=user_id)
        except Admin.DoesNotExist:
            return None
