from django.contrib import admin
from django.contrib.admin.models import LogEntry as DjangoLogEntry

admin.site.register(DjangoLogEntry)


# Register your models here.
