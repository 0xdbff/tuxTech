from django.urls import path
from . import views

urlpatterns = [
    path("api/support/list", views.SupportListView.as_view(), name="support-list"),
    path(
        "api/support/<uuid:pk>/",
        views.SupportDetailView.as_view(),
        name="support-detail",
    ),
]
