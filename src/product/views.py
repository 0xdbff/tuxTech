from django.http import HttpResponseForbidden
from rest_framework.permissions import IsAuthenticated

from django.views import View

from .models import Category
from .models import Variant
from .models import Brand
from .models import BaseInfo
from .models import Media
from .models import Comment

from django.http import JsonResponse

from rest_framework import generics
from .serializers import CategorySerializer
from .serializers import BaseInfoSerializer
from .serializers import CommentSerializer
from .serializers import BrandSerializer


class CategoryList(generics.ListAPIView):
    """ """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated]


def get_media(request):
    """ """

    if not request.user.is_authenticated:
        return HttpResponseForbidden("User not authenticated")

    print(request.user.is_authenticated)

    media_items = Media.objects.filter(image__isnull=False)
    media_list = [
        {
            "id": media.id,
            "name": media.name,
            "media_type": media.media_type,
            "url": media.image.url,
        }
        for media in media_items
    ]
    return JsonResponse(media_list, safe=False)


class ProductsByCategoryView(View):
    """ """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        category = self.kwargs["category"]
        products = BaseInfo.objects.filter(category__name=category)
        data = {
            "products": [
                {
                    "ref": product.ref,
                    "name": product.name,
                    "description": product.description,
                    "variants": [
                        {
                            "sku": variant.sku,
                            "name": variant.name,
                            "price": variant.price,
                            "stock": variant.stock,
                            "stock_value": variant.stock_value,
                        }
                        for variant in product.Variant.all()
                    ],
                }
                for product in products
            ]
        }
        return JsonResponse(data)


class ProductsBySubCategoryView(View):
    """ """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        subcategory = self.kwargs["subcategory"]
        products = BaseInfo.objects.filter(subCategory__name=subcategory)
        data = {
            "products": [
                {
                    "ref": product.ref,
                    "name": product.name,
                    "description": product.description,
                    "variants": [
                        {
                            "sku": variant.sku,
                            "name": variant.name,
                            "price": variant.price,
                            "stock": variant.stock,
                            "stock_value": variant.stock_value,
                        }
                        for variant in product.Variant.all()
                    ],
                }
                for product in products
            ]
        }
        return JsonResponse(data)


class ProductsByBrandView(View):
    """ """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        brand = self.kwargs["brand"]
        products = BaseInfo.objects.filter(brand__name=brand)
        data = {
            "products": [
                {
                    "ref": product.ref,
                    "name": product.name,
                    "description": product.description,
                    "variants": [
                        {
                            "sku": variant.sku,
                            "name": variant.name,
                            "price": variant.price,
                            "stock": variant.stock,
                            "stock_value": variant.stock_value,
                        }
                        for variant in product.Variant.all()
                    ],
                }
                for product in products
            ]
        }
        return JsonResponse(data)


class BaseInfoList(generics.ListCreateAPIView):
    """ """

    permission_classes = [IsAuthenticated]

    queryset = BaseInfo.objects.all()
    serializer_class = BaseInfoSerializer


class BaseInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    """ """

    permission_classes = [IsAuthenticated]

    queryset = BaseInfo.objects.all()
    serializer_class = BaseInfoSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List all comments for a given variant, or create a new comment.

    * The GET method retrieves a list of all comments for a given variant.
    * The POST method allows clients to create a new comment for a variant.
    """

    serializer_class = CommentSerializer

    def get_queryset(self):
        variant_pk = self.kwargs["variant_pk"]
        variant = Variant.objects.get(pk=variant_pk)
        return Comment.objects.filter(variant=variant)

    def perform_create(self, serializer):
        variant_pk = self.kwargs["variant_pk"]
        variant = Variant.objects.get(pk=variant_pk)
        serializer.save(variant=variant)


class CommentDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment or delete a comment.

    * The GET method retrieves a specific comment.
    * The DELETE method allows clients to delete a specific comment.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BrandListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
