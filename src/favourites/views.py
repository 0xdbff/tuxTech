from django.shortcuts import render
from rest_framework import generics
from .models import Info, Item
from .serializers import FavouritesSerializer, ItemSerializer


class FavouritesCreateView(generics.CreateAPIView):
    """
    A view for creating new instances of Info model.
    """

    queryset = Info.objects.all()
    serializer_class = FavouritesSerializer


class FavouritesView(generics.RetrieveUpdateAPIView):
    """
    A view for retrieving and updating instances of Info model.
    """

    queryset = Info.objects.all()
    serializer_class = FavouritesSerializer
    lookup_field = "id"


class ItemCreateView(generics.CreateAPIView):
    """
    A view for creating new instances of Item model.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDeleteView(generics.DestroyAPIView):
    """
    A view for deleting instances of Item model.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"


class ItemView(generics.RetrieveUpdateAPIView):
    """
    A view for retrieving and updating instances of Item model.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"
