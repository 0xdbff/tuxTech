
from django.contrib.auth.management.commands import (
     createsuperuser as base_createsuperuser,
 )
from ...models import Admin


class Command(base_createsuperuser.Command):
     help = "Create a new superuser, either a Client or an Admin"

     def handle(self, *args, **options):
         model = Admin

         self.UserModel = model
         super().handle(*args, **options)

# users/management/commands/createsuperuser.py

# from django.contrib.auth.management.commands import (
#     createsuperuser as base_createsuperuser,
# )
# from ...models import Admin
#
#
# class Command(base_createsuperuser.Command):
#     help = "Create a new superuser (Admin)"
#
#     def handle(self, *args, **options):
#         options["interactive"] = True
#         options.setdefault("username_field", "email")
#         return super(Command, self).handle(*args, **options)
#
#     def get_user_model(self):
#         return Admin
