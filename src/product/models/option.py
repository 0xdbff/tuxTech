""" """
from django.db import models
import uuid


class Option(models.Model):
    """ """

    Id = models.PositiveSmallIntegerField(primary_key=True, editable=True)
    spec_id = models.ForeignKey(
        "Specification",
        on_delete=models.CASCADE,
        related_name="base_info",
        editable=False,
        null=False,
    )
    price_to_add = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        """Instance name"""
        display_value = self.spec_id.value[:32] + (
            " (...) " if len(self.spec_id.value) > 32 else ""
        )
        return f"{self.spec_id.key} - ({display_value})"

    # class Meta:
    #     ordering = ["-key"]
