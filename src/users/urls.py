from django.urls import path
from .views import LoginView
from .views import ClientJsonView

urlpatterns = [
    path("api/login/", LoginView.as_view(), name="login"),
    path("clients/<uuid:client_id>/", ClientJsonView.as_view(), name="client_json"),
]
