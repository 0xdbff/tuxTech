from django.urls import path
from .views import LoginView, AdminLoginView, ClientJsonView, ClientRegistrationView

urlpatterns = [
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/admin/login/", AdminLoginView.as_view(), name="login"),
    path("clients/<uuid:client_id>/", ClientJsonView.as_view(), name="client_json"),
    path("register/", ClientRegistrationView.as_view(), name="register"),
]
