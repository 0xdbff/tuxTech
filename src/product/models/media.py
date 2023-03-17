""" Product models"""
from django.db import models
from .variant import Variant

class Media(models.Model):
    """
    Media model to represent images, videos, or gifs associated with a product variant.
    Typically, there will be 4 or more media items for every product variant when available.
    """

    filename = models.CharField(max_length=21, primary_key=True, editable=False)
    """the filename will be a media hash"""
    media_type = models.CharField(max_length=4)
    """Media type -> url, png, jpg, gif ..."""
    pos = models.PositiveSmallIntegerField(null=False)
    """pos 0 for variant equals preview image"""
    variant_id = models.ForeignKey(
        Variant, on_delete=models.CASCADE, related_name="Variant_image"
    )

    def __str__(self):
        """Instance name"""
        return f"{self.variant_id.name} : MEDIA@({self.pos})"
