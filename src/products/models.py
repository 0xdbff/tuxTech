""" Product models"""
from django.db import models


class Specification(models.Model):
    """ """

    name = models.CharField(max_length=128)
    id = models.UUIDField(primary_key=True)

    def __str__(self):
        """Instance name"""
        return self.name


class Categorie(models.Model):
    """Product's categorie ex: Computer, Server..."""

    name = models.CharField(max_length=128)
    id = models.UUIDField(primary_key=True)

    def __str__(self):
        """Instance name"""
        return self.name


class Brand(models.Model):
    """Product's Brand ex: Amd"""

    name = models.CharField(max_length=128)
    id = models.UUIDField(primary_key=True)

    def __str__(self):
        """Instance name"""
        return self.name


class Product(models.Model):
    """A product for the store"""

    name = models.CharField(max_length=512)
    id = models.UUIDField(primary_key=True)

    def __str__(self):
        """Instance name"""
        return self.name
