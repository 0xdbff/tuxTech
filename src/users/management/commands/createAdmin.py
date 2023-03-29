from django.core.management.base import BaseCommand
from ...models import Admin


class Command(BaseCommand):
    help = "Create a new admin superuser"

    def handle(self, *args, **options):
        email = input("Email: ")
        username = input("Username: ")
        password = input("Password: ")

        admin = Admin.objects.create_superuser(
            email=email, username=username, password=password
        )
        admin.save()

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created admin superuser {admin}")
        )
