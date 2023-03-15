""" """
from django.db import models
import uuid

class Specification(models.Model):
    """
    Specification model to store individual product specifications.
    Each specification consists of a name and a value (e.g., color: red).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    value = models.TextField(null=False)
    # SET comparison methods

    def __str__(self):
        """Instance name"""
        return self.name
