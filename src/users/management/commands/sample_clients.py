import random
from django.core.management.base import BaseCommand
from users.models import Client


class Command(BaseCommand):
    help = "Populate the database with sample clients"

    def handle(self, *args, **options):
        sample_emails = [
            "example1@example.com",
            "example2@example.com",
            "example3@example.com",
            "example4@example.com",
            "example5@example.com",
            "example6@example.com",
            "example7@example.com",
            "example8@example.com",
            "example9@example.com",
            "example10@example.com",
        ]

        for email in sample_emails:
            nif = str(random.randint(10000000, 99999999)) + "X"
            username = email.split("@")[0]
            receive_news = random.choice([True, False])

            Client.objects.create(
                nif=nif,
                email=email,
                username=username,
                receive_news=receive_news,
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated sample clients"))
