from rest_framework import viewsets
from .models import Order, OrderedItem
from .serializers import OrderSerializer, OrderedItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderedItemViewSet(viewsets.ModelViewSet):
    queryset = OrderedItem.objects.all()
    serializer_class = OrderedItemSerializer
