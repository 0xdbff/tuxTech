from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameModelBackend(BaseBackend):
    """ """

    def authenticate(self, request, input=None, password=None, **kwargs):
        """ """
        try:
            user = User.objects.get(email=input)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=input)
            except User.DoesNotExist:
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
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
