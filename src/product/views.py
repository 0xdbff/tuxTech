from django.shortcuts import render
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
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def get_media(request):
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


class ProductsBySubCategoryView(View):
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
    queryset = BaseInfo.objects.all()
    serializer_class = BaseInfoSerializer

class BaseInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseInfo.objects.all()
    serializer_class = BaseInfoSerializer

