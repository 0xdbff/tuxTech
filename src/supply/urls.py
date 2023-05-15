from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/supplier/new/",
        views.SupplierCreateView.as_view(),
        name="supplier-create",
    ),
    path(
        "api/supplier/<uuid:id>",
        views.SupplierRetrieveView.as_view(),
        name="supplier-get-by-id",
    ),
    path("api/info/new", views.InfoCreateView.as_view(), name="info-create"),
    path("api/info/<uuid:id>", views.InfoRetrieveView.as_view(), name="info-get-by-id"),
]
