from django.db import models, transaction
from .unit import Unit
from .media import Media
from .specification import Specification
import uuid


def generate_unique_sku():
    return uuid.uuid4().hex


class VariantManager(models.Manager):
    def set_default_variant(self, variant):
        with transaction.atomic():
            self.filter(is_default=True).update(is_default=False)
            variant.is_default = True
            variant.save()


class Variant(models.Model):
    """
    A variant of a product ex Phone with a color.
    """

    ean = models.CharField(max_length=14, unique=True, editable=False)
    """ """
    sku = models.CharField(
        max_length=32, primary_key=True, editable=False, default=generate_unique_sku
    )
    """ """
    is_default = models.BooleanField(null=False, editable=True, default=False)
    """ """
    name = models.TextField(null=False)
    """ """
    media = models.ManyToManyField(Media, through="VariantMedia")
    """ """
    mediafiles_hash = models.CharField(max_length=64, editable=True)
    """ Dont resend media to website if there are no differences for this variant."""
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    """ """
    info = models.ForeignKey(
        "BaseInfo",
        on_delete=models.CASCADE,
        related_name="Variant",
        null=False,
    )
    """ """
    specifications = models.ManyToManyField(Specification)
    """ """
    altered_specs = models.JSONField(null=True, editable=False)
    """ """

    objects = VariantManager()
    """ """

    def save(self, *args, **kwargs):
        """ """
        self._calculate_altered_specifications()

        if self.is_default:
            Variant.objects.exclude(pk=self.pk).update(is_default=False)
        super().save(*args, **kwargs)

    @property
    def stock(self):
        """ """
        return Unit.objects.filter(variant_info=self).count()

    @property
    def stock_value(self):
        """ """
        return self.stock * self.price

    @property  # !TODO
    def gen_sku(self):
        """ """
        return f"{self.info.Variant._sku_prefix}"

    def _calculate_altered_specifications(self):
        """ """
        if self.is_default:
            self.altered_specifications = None
            return

        default_variant = Variant.objects.filter(_is_default=True).first()
        if not default_variant:
            return

        altered_specs = {}
        default_specs = set(default_variant.specifications.all())
        current_specs = set(self.specifications.all())

        for spec in current_specs - default_specs:
            altered_specs[spec.key] = spec.value

        for spec in default_specs - current_specs:
            altered_specs[spec.key] = None

        self.altered_specifications = altered_specs
