""" """
from enum import unique
from django.db import models
from .custom_user import TuxTechUser


class Client(TuxTechUser):
    """ """

    user = models.OneToOneField(
        TuxTechUser, on_delete=models.CASCADE, related_name="Client", unique=True
    )
    nif = models.CharField(max_length=16, unique=True, null=True, blank=True)
    receive_news = models.BooleanField(default=False)
    cart = models.OneToOneField(
        "cart.info", on_delete=models.CASCADE, null=True, blank=True
    )
    favourites = models.OneToOneField(
        "favourites.info",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
