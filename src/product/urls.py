from django.urls import path
from . import views
from .views import (
    ProductsByCategoryView,
    ProductsBySubCategoryView,
    ProductsByBrandView,
)

urlpatterns = [
    # ... other urlpatterns ...
    path("api/media/", views.get_media, name="get_media"),
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
]
