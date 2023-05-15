from django.urls import path
from .views import OrderListView, OrderCreateUpdateView

urlpatterns = [
    path("api/orders/", OrderListView.as_view(), name="order-list"),
    path("api/orders/<uuid:pk>/", OrderCreateUpdateView.as_view(), name="order-detail"),
]
