from rest_framework import generics
from .models import Info, Supplier
from .serializers import SupplySerializer, SupplierSerializer


class SupplierCreateView(generics.CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierRetrieveView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = "id"


class InfoCreateView(generics.CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = SupplySerializer


class InfoRetrieveView(generics.RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = SupplySerializer
    lookup_field = "id"
