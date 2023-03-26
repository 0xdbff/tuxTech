from django.urls import path
from . import views

urlpatterns = [
    # ... other urlpatterns ...
    path('api/media/', views.get_media, name='get_media'),
]
