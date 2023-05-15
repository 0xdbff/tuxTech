from django.contrib import admin

from .models import PromotionApplication, Promotion, AdvertisementContract

admin.register(PromotionApplication)
admin.register(Promotion)


@admin.register(AdvertisementContract)
class AdvertisementContractAdmin(admin.ModelAdmin):
    list_display = ["start_date", "end_date", "ad_text", "priority"]
