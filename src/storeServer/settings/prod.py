from .base import *

# !TODO change
DEBUG = True

# ALLOWED_HOSTS = [
#     "gldb.dev",
#     "www.gldb.dev",
#     "176.79.170.121",
# ]
ALLOWED_HOSTS = [
    "gldb.dev",
    "www.gldb.dev",
    "176.79.170.121",
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
]

# !TODO
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-kluzk8h%5eq7$()&s_zn_@=is=#0i5r$ap0@gwj8(c^2_b7c2y"

# dev
CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = ["https://gldb.dev:8443", "https://www.gldb.dev:8443"]

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        # !TODO
        "NAME": "djangodev",
        "USER": "postgres",
        "PASSWORD": os.environ.get("TUXTECH_POSTGRES_PASSWD"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

MEDIA_ROOT = "/srv/nginx/tuxTech/media"
STATIC_ROOT = "/srv/nginx/tuxTech/static/"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.gldb.dev"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "home@gldb.dev"
EMAIL_HOST_PASSWORD = os.environ.get("TUXTECH_MAIL_PASSWD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
