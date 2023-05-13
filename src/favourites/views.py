from django.shortcuts import render
from rest_framework import generics
from .models import Info, Item
from .serializers import FavouritesSerializer, ItemSerializer


class FavouritesCreateView(generics.CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = FavouritesSerializer


class FavouritesView(generics.RetrieveUpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = FavouritesSerializer


class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemView(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
