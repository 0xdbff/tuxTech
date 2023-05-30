from django.urls import path
from . import views
from .views import (
    ProductsByCategoryView,
    ProductsBySubCategoryView,
    ProductsByBrandView,
    CategoryList,
    BaseInfoList,
    BaseInfoDetail,
    CommentList,
    CommentDetail,
    BrandListView,
)

urlpatterns = [
    path("api/media/", views.get_media, name="get_media"),
    path("api/brands/", BrandListView.as_view(), name="brands-list"),
    path(
        "api/category/<str:category>/",
        ProductsByCategoryView.as_view(),
        name="products_by_category",
    ),
    path(
        "api/subcategory/<str:subcategory>/",
        ProductsBySubCategoryView.as_view(),
        name="products_by_subcategory",
    ),
    path(
        "api/brand/<str:brand>/",
        ProductsByBrandView.as_view(),
        name="products_by_brand",
    ),
    path("api/categories/", CategoryList.as_view(), name="categories-list"),
    path("api/base_info/", BaseInfoList.as_view(), name="base_info_list"),
    path("api/<uuid:pk>/", BaseInfoDetail.as_view(), name="base_info_detail"),
    path("api/variants/<uuid:id>/comments/", CommentList.as_view()),
    path("api/comments/<int:id>/", CommentDetail.as_view()),
]
