from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from users.models import Client


class Promotion(models.Model):
    """
    A model representing a promotion.
    """

    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    discount_percentage = models.DecimalField(max_digits=3, decimal_places=2, null=True)

    def is_active(self):
        """
        Determine if the promotion is currently active.

        Returns:
            bool: True if the promotion is active, False otherwise.
        """
        now = timezone.now()
        return self.start_date <= now <= self.end_date


class PromotionApplication(models.Model):
    """
    A model representing a promotion application to a product variant.
    """

    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    variant = models.ForeignKey("product.Variant", on_delete=models.CASCADE)

    def notify_clients(self):
        """
        Notify all subscribed clients about a promotion.
        """
        if self.promotion.is_active():
            subscribed_clients = Client.objects.filter(receive_news=True)
            for client in subscribed_clients:
                send_mail(
                    "Promotion on your favorite product",
                    f"The product {self.variant.name} is on promotion!\n\n"
                    + "Best regards!\n The TuxTech team!",
                    "home@gldb.dev",
                    [client.email],
                    fail_silently=False,
                )


class AdvertisementContract(models.Model):
    """
    AdvertisementContract model to store information about advertisement contracts.
    """

    start_date = models.DateField()
    end_date = models.DateField()
    advertisement_image = models.ImageField(upload_to="advertisements/")
    ad_text = models.TextField()
    priority = models.PositiveIntegerField(null=True, default=1)
