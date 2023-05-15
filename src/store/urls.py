from django.urls import path
from .views import PromotionApplicationList

urlpatterns = [
    path("api/promotions/", PromotionApplicationList.as_view()),
]
