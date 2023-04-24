from django.contrib import admin
from .models import TuxTechUser

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import TuxTechUser, Client
from django.utils.translation import gettext_lazy as _


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = TuxTechUser
        fields = "__all__"


class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    list_display = ("email", "username", "is_staff", "is_superuser")
    search_fields = ("email", "username")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("username", "first_name", "last_name", "gender")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )


class ClientAdmin(admin.ModelAdmin):
    list_display = ("user", "nif", "receive_news")
    fields = ("user", "nif", "receive_news", "cart", "favourites")
    search_fields = ("nif",)


admin.site.register(TuxTechUser, UserAdmin)
admin.site.register(Client, ClientAdmin)
