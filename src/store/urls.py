from django.urls import path
from .views import PromotionApplicationList, AdvertisementContractView

urlpatterns = [
    path("api/promotions/", PromotionApplicationList.as_view()),
    path(
        "api/advertisements/", AdvertisementContractView.as_view(), name="advertisement"
    ),
]
