from django.urls import path
from .views import CartInfoCreateView, CartInfoView, ItemCreateView, ItemView

urlpatterns = [
    path("api/new/", CartInfoCreateView.as_view(), name="cart-create"),
    path("api/<int:pk>/", CartInfoView.as_view(), name="cart"),
    path("api/item/new/", ItemCreateView.as_view(), name="item-create"),
    path("api/item/<int:pk>/", ItemView.as_view(), name="item"),
]
