from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("api/login/", views.LoginView.as_view(), name="login"),
    path("api/refresh_token/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/client/register/", views.ClientRegistrationView.as_view(), name="register"
    ),
    path(
        "api/client/<uuid:id>/",
        views.ClientView.as_view(),
        name="client-update",
    ),
    path(
        "api/client/address/new/",
        views.AddressCreateView.as_view(),
        name="address-create",
    ),
    path(
        "api/client/address/dev_null/<uuid:id>",
        views.AddressDeleteView.as_view(),
        name="credit_card_create",
    ),
    path(
        "api/client/address/<uuid:id>/",
        views.AddressView.as_view(),
        name="address-update",
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
    path(
        "api/client/credit_card/new/",
        views.CreditCardCreateView.as_view(),
        name="credit_card_create",
    ),
    path(
        "api/client/credit_card/dev_null/<uuid:id>",
        views.CreditDeleteView.as_view(),
        name="credit_card_create",
    ),
    path(
        "api/client/credit_card/<uuid:id>/",
        views.CreditCardView.as_view(),
        name="credit_card_update",
    ),
]
