from django.db import models
from .media import Media
from .variant import Variant


class VariantMedia(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    pos = models.PositiveSmallIntegerField(null=False)
    """pos 0 for variant equals preview image"""

    class Meta:
        unique_together = ("variant", "media")
