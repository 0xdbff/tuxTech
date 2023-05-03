from django.urls import path
from .views import LoginView, AdminLoginView, ClientJsonView, ClientRegistrationView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/refresh_token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("clients/<uuid:client_id>/", ClientJsonView.as_view(), name="client_json"),
    path("register/", ClientRegistrationView.as_view(), name="register"),
]
