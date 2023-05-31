from rest_framework import generics
from .models import Info, Supplier
from .serializers import SupplySerializer, SupplierSerializer

class SupplierCreateView(generics.CreateAPIView):
    """
    A view for creating new instances of the Supplier model.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierRetrieveView(generics.RetrieveAPIView):
    """
    A view for retrieving instances of the Supplier model.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = "id"


class InfoCreateView(generics.CreateAPIView):
    """
    A view for creating new instances of the Info model.
    """
    queryset = Info.objects.all()
    serializer_class = SupplySerializer


class InfoRetrieveView(generics.RetrieveAPIView):
    """
    A view for retrieving instances of the Info model.
    """
    queryset = Info.objects.all()
    serializer_class = SupplySerializer
    lookup_field = "id"

