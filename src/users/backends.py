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
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Client.objects.get(username=username)
            if password and user.check_password(password):
                return user
        except Client.DoesNotExist:
            pass

        # try:
        #     user = Admin.objects.get(username=username)
        #     if password and user.check_password(password):
        #         print(f"Found user by username: {username}, in Client")
        #         return user
        # except Admin.DoesNotExist:
        #     print("User does not exist")
        #     pass

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            pass

        # try:
        #     return Admin.objects.get(pk=user_id)
        # except Admin.DoesNotExist:
        #     pass
