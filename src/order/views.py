from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderListView(generics.GenericAPIView, mixins.ListModelMixin):
    """Handles requests for order lists.

    Attributes:
        serializer_class: The serializer class to be used.

    Methods:
        get_queryset: Filters the orders related to the authenticated user.
        get: Handles the GET requests.
    """
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):
        """Filter the orders related to the authenticated user.

        Returns:
            A QuerySet with orders related to the authenticated user.
        """
        return Order.objects.filter(customer=self.request.user)

    def get(self, request, *args, **kwargs):
        """Handle the GET request.

        Args:
            request: The request instance.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            The list of orders related to the authenticated user.
        """
        return self.list(request, *args, **kwargs)


class OrderCreateUpdateView(
    generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin
):
    permission_classes = [IsAuthenticated]

    """Handles requests for creating and updating orders.

    Attributes:
        serializer_class: The serializer class to be used.
        queryset: The queryset to be used.

    Methods:
        post: Handles the POST requests.
        put: Handles the PUT requests.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        """Handle the POST request.

        Args:
            request: The request instance.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            The newly created order instance.
        """
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Handle the PUT request.

        Args:
            request: The request instance.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            The updated order instance.
        """
        return self.update(request, *args, **kwargs)
