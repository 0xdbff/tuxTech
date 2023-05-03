from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from rest_framework.permissions import IsAuthenticated

from django.views import View

from .models import Category
from .models import Variant
from .models import Brand
from .models import BaseInfo
from .models import Media

from django.http import JsonResponse

from rest_framework import generics
from .serializers import CategorySerializer
from .serializers import BaseInfoSerializer


class CategoryList(generics.ListAPIView):
    """ """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden("User not authenticated")
    #     return super().dispatch(request, *args, **kwargs)


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
                    "ean": product.ean,
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

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden("User not authenticated")
    #     return super().dispatch(request, *args, **kwargs)


class ProductsBySubCategoryView(View):
    """ """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        subcategory = self.kwargs["subcategory"]
        products = BaseInfo.objects.filter(subCategory__name=subcategory)
        data = {
            "products": [
                {
                    "ean": product.ean,
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
                    "ean": product.ean,
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
