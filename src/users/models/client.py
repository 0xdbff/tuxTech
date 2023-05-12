""" """
from enum import unique
from django.db import models
from .custom_user import TuxTechUser


class Client(TuxTechUser):
    """ """

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
    default_invoice_address = models.ForeignKey(
        "users.Address",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clients_invoice_address",
    )
    default_shipping_address = models.ForeignKey(
        "users.Address",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clients_shipping_address",
    )
    default_credit_card = models.OneToOneField(
        "users.CreditCard",
        related_name="clients_credit_card",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_enterprise = models.BooleanField(default=False)
