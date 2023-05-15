from django.shortcuts import render
from rest_framework import generics
from .models import Info, Item
from .serializers import CartInfoSerializer, ItemSerializer


class CartInfoCreateView(generics.CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = CartInfoSerializer


class CartInfoView(generics.RetrieveUpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = CartInfoSerializer
    lookup_field = "id"


class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"


class ItemView(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"
