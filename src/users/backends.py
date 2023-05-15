# from django.contrib.auth.backends import BaseBackend
#
# # from django.contrib.auth import get_user_model
# from .models import Admin, Client
#
#
# class CustomModelBackend(BaseBackend):
#     def get_user_by_credentials(self, user_model, input, password):
#         """
#         Attempt to get a user from the given model by email or username
#         and check if the provided password matches.
#         """
#         user = None
#
#         try:
#             user = user_model.objects.get(email=input)
#             print(f"Found user by email: {input}, {user_model}")
#         except user_model.DoesNotExist:
#             print(f"User not found by email: {input}, {user_model}")
#             try:
#                 user = user_model.objects.get(username=input)
#                 print(f"Found user by username: {input}, {user_model}")
#             except user_model.DoesNotExist:
#                 print(f"User not found by username: {input}, {user_model}")
#                 return None
#
#         if user and user.check_password(password):
#             print(f"Password matches for user: {input}, {user_model}")
#             return user
#         else:
#             print(f"Password does not match for user: {input}, {user_model}")
#
#         return None
#
#     def authenticate(
#         self, request, input=None, password=None, admin_only=False, **kwargs
#     ):
#         if not admin_only:
#             # Try to authenticate as a Client
#             user = self.get_user_by_credentials(Client, input, password)
#             if user is not None:
#                 return user
#
#         # Try to authenticate as an Admin
#         user = self.get_user_by_credentials(Admin, input, password)
#         if user is not None:
#             return user
#
#         return None
#
#     def get_user(self, user_id):
#         try:
#             print("     7          ")
#             return Client.objects.get(pk=user_id)
#         except Client.DoesNotExist:
#             try:
#                 print("     8          ")
#                 return Admin.objects.get(pk=user_id)
#             except Admin.DoesNotExist:
#                 print("     9          ")
# return None

from django.contrib.auth.backends import BaseBackend
from .models import Client


class CustomModelBackend(BaseBackend):
    """
    Custom authentication backend for authenticating users based on the Client model.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticates a user based on the provided username and password.
        :param request: The request object.
        :param str username: The username of the user.
        :param str password: The password of the user.
        :return: The authenticated user if successful, None otherwise.
        :rtype: users.models.Client
        """
        try:
            user = Client.objects.get(username=username)
            if password and user.check_password(password):
                return user
        except Client.DoesNotExist:
            pass

    def get_user(self, user_id):
        """
        Retrieves a user based on the provided user ID.
        :param int user_id: The ID of the user.
        :return: The user with the given ID if found, None otherwise.
        :rtype: users.models.Client
        """
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            pass

        # try:
        #     return Admin.objects.get(pk=user_id)
        # except Admin.DoesNotExist:
        #     pass
