""" """
from django.db import models


class Category(models.Model):
    """
    Category model to represent different product categories.
    Examples include Computers, Servers, and Mobile Devices.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=False)
    description = models.TextField()

    def __str__(self):
        """Instance name"""
        return self.name
