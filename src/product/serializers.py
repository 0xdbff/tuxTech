from rest_framework import serializers
from .models import BaseInfo, Variant, Media, VariantMedia, Category, Comment, Brand


class MediaSerializer(serializers.ModelSerializer):
    """
    Serializer for the Media model.

    Serializes the Media model fields.
    """

    class Meta:
        model = Media
        fields = ("id", "name", "media_type", "image")


class VariantMediaSerializer(serializers.ModelSerializer):
    """
    Serializer for the VariantMedia model.

    Serializes the VariantMedia model fields.
    Includes a nested MediaSerializer to serialize the related Media model.
    """

    media = MediaSerializer()

    class Meta:
        model = VariantMedia
        fields = ("media", "pos")


class VariantSerializer(serializers.ModelSerializer):
    """
    Serializer for the Variant model.

    Serializes the Variant model fields.
    Includes a nested VariantMediaSerializer to serialize the related VariantMedia models.
    """

    medias = VariantMediaSerializer(
        source="variantmedia_set", many=True, read_only=True
    )

    class Meta:
        model = Variant
        fields = ("sku", "ean", "is_default", "name", "price", "medias")


class BaseInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for the BaseInfo model.

    Serializes the BaseInfo model fields.
    Includes additional SerializerMethodFields to customize serialization of related models.
    """

    default_variant = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = BaseInfo
        fields = (
            "name",
            "ref",
            "description",
            "details",
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
        """
        Retrieve the default Variant for the BaseInfo model.

        Returns the serialized data of the default Variant using the VariantSerializer.
        """
        default_variant = Variant.objects.filter(info=obj, is_default=True).first()
        if default_variant:
            return VariantSerializer(default_variant).data
        return None

    def get_thumbnail(self, obj):
        """
        Retrieve the thumbnail VariantMedia for the default Variant of the BaseInfo model.

        Returns the serialized data of the thumbnail VariantMedia using the MediaSerializer.
        """
        default_variant = Variant.objects.filter(info=obj, is_default=True).first()
        if default_variant:
            thumbnail = VariantMedia.objects.filter(
                variant=default_variant, pos=0
            ).first()
            if thumbnail:
                return MediaSerializer(thumbnail.media).data
        return None


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.

    Serializes the Category model fields.
    """

    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    Serializes the Comment model fields.
    """

    class Meta:
        model = Comment
        fields = ["client", "variant", "content", "date_posted"]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'logo_hash', 'logo_type', 'logo', 'date_added']

