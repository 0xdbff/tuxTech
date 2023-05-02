from django.urls import path
from . import views
from .views import (
    ProductsByCategoryView,
    ProductsBySubCategoryView,
    ProductsByBrandView,
    CategoryList,
    BaseInfoList,
    BaseInfoDetail,
)

urlpatterns = [
    path("media/", views.get_media, name="get_media"),
    path(
        "category/<str:category>/",
        ProductsByCategoryView.as_view(),
        name="products_by_category",
    ),
    path(
        "subcategory/<str:subcategory>/",
        ProductsBySubCategoryView.as_view(),
        name="products_by_subcategory",
    ),
    path("brand/<str:brand>/", ProductsByBrandView.as_view(), name="products_by_brand"),
    path("api/categories/", CategoryList.as_view(), name="categories-list"),
    path("api/base_info/", BaseInfoList.as_view(), name="base_info_list"),
    path('<uuid:pk>/', BaseInfoDetail.as_view(), name='base_info_detail'),
]
