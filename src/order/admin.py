from django.contrib import admin

from .models import Order, OrderedItem

admin.register(Order)
admin.register(OrderedItem)
