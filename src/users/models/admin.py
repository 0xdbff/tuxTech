
from django.db import models

from .custom_user import CustomUser


class Admin(CustomUser):
    receive_news = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="admin_set",
        related_query_name="admin",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="admin_set",
        related_query_name="admin",
        verbose_name="user permissions",
    )
