from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("api/login/", views.LoginView.as_view(), name="login"),
    path("api/refresh_token/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/client/<uuid:client_id>/",
        views.ClientJsonView.as_view(),
        name="client_json",
    ),
    path(
        "api/register/add-address/", views.AddAddressView.as_view(), name="add_address"
    ),
    path(
        "api/register/get-countries/",
        views.ListCountriesView.as_view(),
        name="list_countries",
    ),
    path(
        "api/register/get-cities/",
        views.ListCitiesView.as_view(),
        name="list_cities",
        # api/register/get-cities/?country=<country_id>
    ),
    path("api/register/", views.ClientRegistrationView.as_view(), name="register"),
]
