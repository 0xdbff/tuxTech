from django.urls import path
from .views import (
    FavouritesCreateView,
    FavouritesView,
    ItemCreateView,
    ItemView,
    ItemDeleteView,
)

urlpatterns = [
    path("api/new/", FavouritesCreateView.as_view(), name="favourites-create"),
    path("api/<uuid:id>/", FavouritesView.as_view(), name="favourites"),
    path("api/item/new/", ItemCreateView.as_view(), name="item-create"),
    path("api/item/<uuid:id>/", ItemView.as_view(), name="item"),
    path("api/item/dev_null/<uuid:id>/", ItemDeleteView.as_view(), name="item"),
]
