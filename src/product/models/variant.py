from django.db import models
from .unit import Unit
from .media import Media


class Variant(models.Model):
    """
    A variant of a product ex Phone with a color.
    """

    sku = models.CharField(max_length=32, primary_key=True, editable=False)
    variant_pos = models.SmallIntegerField(editable=True, null=False)
    name = models.TextField(null=False)
    media = models.ManyToManyField(Media, through="VariantMedia")
    mediafiles_hash = models.CharField(max_length=64, editable=True)
    """ Dont resend media to website if there are no differences for this variant."""
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    info = models.ForeignKey(
        "BaseInfo",
        on_delete=models.CASCADE,
        related_name="Variant",
        null=False,
        editable=False,
    )

    @property
    def stock(self):
        return Unit.objects.filter(variant_info=self).count()

    @property
    def stock_value(self):
        return self.stock * self.price
