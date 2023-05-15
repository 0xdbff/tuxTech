from rest_framework import serializers
from .models import BaseInfo, Variant, Media, VariantMedia, Category, Comment


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ("id", "name", "media_type", "image")


class VariantMediaSerializer(serializers.ModelSerializer):
    media = MediaSerializer()

    class Meta:
        model = VariantMedia
        fields = ("media", "pos")


class VariantSerializer(serializers.ModelSerializer):
    medias = VariantMediaSerializer(
        source="variantmedia_set", many=True, read_only=True
    )

    class Meta:
        model = Variant
        fields = ("sku", "ean", "is_default", "name", "price", "medias")


class BaseInfoSerializer(serializers.ModelSerializer):
    default_variant = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = BaseInfo
        fields = (
            "name",
            "ref",
            "description",
            "category",
            "subCategory",
            "ptype",
            "brand",
            "date_added",
            "default_variant",
            "thumbnail",
            "price_min",
            "price_max",
        )

    def get_default_variant(self, obj):
        default_variant = Variant.objects.filter(info=obj, is_default=True).first()
        if default_variant:
            return VariantSerializer(default_variant).data
        return None

    def get_thumbnail(self, obj):
        default_variant = Variant.objects.filter(info=obj, is_default=True).first()
        if default_variant:
            thumbnail = VariantMedia.objects.filter(
                variant=default_variant, pos=0
            ).first()
            if thumbnail:
                return MediaSerializer(thumbnail.media).data
        return None


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["client", "variant", "content", "date_posted"]
