from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from cities.models import City, Country
from datetime import date
from .validators import validate_card_number
import uuid


class CreditCard(models.Model):
    CARD_TYPES = (
        ("VISA", "Visa"),
        ("MASTERCARD", "Mastercard"),
        ("UNKNOWN", "Unknown"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, related_name="credit_cards"
    )
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16, validators=[validate_card_number])
    card_type = models.CharField(max_length=10, choices=CARD_TYPES, default="UNKNOWN")
    expiry_month = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    expiry_year = models.PositiveIntegerField(
        validators=[MinValueValidator(date.today().year)]
    )
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.cardholder_name}: **** **** **** {self.card_number[-4:]}"

    def save(self, *args, **kwargs):
        self.card_type = self.get_card_type()
        super(CreditCard, self).save(*args, **kwargs)

    def get_card_type(self):
        if self.card_number.startswith("4"):
            return "VISA"
        elif self.card_number.startswith(("51", "52", "53", "54", "55")):
            return "MASTERCARD"
        else:
            return "UNKNOWN"


class CustomUserManager(BaseUserManager):
    """ """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        return self.create_user(email, password, **extra_fields)


class Client(AbstractBaseUser, PermissionsMixin):
    """ """

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("N", "Prefer not to say"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nif = models.CharField(max_length=16, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="N")
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True)
    is_active = models.BooleanField(default=True)
    receive_news = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="client_set",
        related_query_name="client",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="client_set",
        related_query_name="client",
        verbose_name="user permissions",
    )

    objects = CustomUserManager()

    # Make the email the default identifier for an admin.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Admin(AbstractBaseUser, PermissionsMixin):
    """ """

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
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="admin_set",
        related_query_name="admin",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="admin_set",
        related_query_name="admin",
        verbose_name="user permissions",
    )

    objects = CustomUserManager()

    # Make the email the default identifier for an admin.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EnterpriseClient(Client):
    """ """

    company_name = models.CharField(max_length=255)
    company_nif = models.CharField(max_length=255)

    def __str__(self):
        """ """
        return f"{self.email} - {self.company_name}"


class Address(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    street = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    house_number = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                r"^\d+[a-zA-Z\s\-]*$",
                message="House number can only contain digits, letters, spaces, and hyphens.",
            )
        ],
    )
    apartment_number = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                r"^\d{5}(-\d{4})?$",
                message="Postal code must be in the format '12345' or '12345-6789'.",
            )
        ],
    )

    def __str__(self):
        return f"{self.street} {self.house_number}\n{self.city}, {self.postal_code}, {self.country}"
