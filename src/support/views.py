from rest_framework import generics
from .models import Support
from .serializers import SupportSerializer
from rest_framework.permissions import IsAuthenticated


class SupportListView(generics.ListCreateAPIView):
    """
    API endpoint that allows support tickets to be viewed or created.

    get: Return a list of all the existing support tickets related to the logged-in client.
    post: Create a new support ticket.
    """
    permission_classes = [IsAuthenticated]

    serializer_class = SupportSerializer

    def get_queryset(self):
        """Override to filter Supports by the logged-in client."""
        return Support.objects.filter(client=self.request.user)


class SupportDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single support ticket to be retrieved, updated or deleted.

    get: Return a specific support ticket.
    put: Update a specific support ticket.
    patch: Partially update a specific support ticket.
    delete: Delete a specific support ticket.
    """
    permission_classes = [IsAuthenticated]

    queryset = Support.objects.all()
    serializer_class = SupportSerializer
