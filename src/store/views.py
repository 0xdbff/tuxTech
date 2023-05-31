from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PromotionApplication
from .serializers import PromotionApplicationSerializer
from .models import AdvertisementContract
from .serializers import AdvertisementContractSerializer


class PromotionApplicationList(APIView):
    """
    API View for PromotionApplication model.
    Handles GET and POST requests.
    """

    def get(self, request, format=None):
        """
        Handles GET requests.

        Retrieves a list of all promotion applications and returns them.

        Parameters:
            request: The request instance.
            format: The format for the response data.

        Returns:
            A Response instance with serialized data of all promotion applications.
        """
        promotion_applications = PromotionApplication.objects.all()
        serializer = PromotionApplicationSerializer(promotion_applications, many=True)
        return Response(serializer.data)

    #!SECURITY remove, and use /admin section to manage promotions!
    def post(self, request, format=None):
        """
        Handles POST requests.

        Creates a new promotion application and notifies subscribed clients if the
        submitted data is valid.

        Parameters:
            request: The request instance containing the data for a new promotion application.
            format: The format for the response data.

        Returns:
            A Response instance with either serialized data of the new promotion application
            (if the creation was successful) or with errors (if the creation failed).
        """
        serializer = PromotionApplicationSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.notify_clients()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementContractView(generics.ListAPIView):
    queryset = AdvertisementContract.objects.all()
    serializer_class = AdvertisementContractSerializer
