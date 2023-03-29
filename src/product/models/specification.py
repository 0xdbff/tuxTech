from django.db import models


class Specification(models.Model):
    """
    Specification model to store individual product specifications.
    Each specification consists of a key and a value (e.g., color: red).
    """

    key = models.CharField(max_length=32)
    value = models.TextField(null=False)

    class Meta:
        # unique_together = ("key", "value")
        constraints = [
            models.UniqueConstraint(fields=["key", "value"], name="unique_key_value")
        ]

    def __str__(self):
        """Instance name"""
        return f"{self.key}-{self.value}"

    # def __eq__(self, other):
    #     if isinstance(other, Specification):
    #         return self.key == other.key and self.value == other.value
    #     return False

    def __hash__(self):
        return hash((self.key, self.value))
