"""User models."""
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid


class TuxTechUserManager(BaseUserManager):
    """
    Custom TuxTech user manager.
    """

    def _create_user(
        self, email, username, password, is_staff, is_superuser, **extra_fields
    ):
        """
        Create and save a TuxTech user with the given email, username and password.
        :param str email: user email
        :param str username: user username
        :param str password: user password
        :param bool is_staff: whether user staff or not
        :param bool is_superuser: whether user admin or not
        :return custom_user.models.EmailUser user: user
        :raise ValueError: email is not set
        """
        if not email:
            raise ValueError("The given email must be set")
        if not username:
            raise ValueError("The given username must be set")
        if not password:
            raise ValueError("The given password must be set")
        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        user = self.model(
            email=email,
            username=username,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=timezone.now(),
            date_joined=timezone.now(),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: regular user
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: admin user
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, username, password, **extra_fields)


class AbstractTuxTechUser(AbstractBaseUser, PermissionsMixin):
    """
    Abstract User with the same behaviour as Django's default User.
    AbstractEmailUser does not have username field. Uses email as the
    USERNAME_FIELD for authentication.
    Use this if you need to extend EmailUser.
    Inherits from both the AbstractBaseUser and PermissionMixin.
    The following attributes are inherited from the superclasses:
        * password
        * last_login
        * is_superuser
    """

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("N", "Prefer not to say"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="O")
    username = models.CharField(max_length=128, unique=True, null=True)
    email = models.EmailField(
        _("email address"), max_length=128, unique=True, db_index=True
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    objects = TuxTechUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        abstract = True

    def get_full_name(self):
        """Return the user's full name"""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Return the user's first name."""
        return f"{self.first_name}"

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


#
#
# class TuxTechUser(AbstractTuxTechUser):
#     """
#     Concrete class for the user model.
#     """
#
#     class Meta(AbstractTuxTechUser.Meta):
#         swappable = "AUTH_USER_MODEL"
