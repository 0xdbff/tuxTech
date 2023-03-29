
from django.db import models

from .custom_user import CustomUser

class Client(CustomUser):
    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="client_set",
        related_query_name="client",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="client_set",
        related_query_name="client",
        verbose_name="user permissions",
    )
    # Client-specific fields and methods
    # ...
    nif = models.CharField(max_length=16, unique=True, null=True, blank=True)
    receive_news = models.BooleanField(default=False)
