# pylint: disable=wildcard-import,unused-wildcard-import

from os import environ

from .settings import *

SECRET_KEY = environ["DJANGO_SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = [
    "prihlasky.strom.sk",
]

USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "signups",
        "USER": "signups",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp-relay.gmail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = "noreply@strom.sk"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

ADMINS = [
    ("Martin Mihálik", "mihalik@strom.sk"),
    ("Peter Kovács", "kovacs@strom.sk"),
]

STATIC_ROOT = BASE_DIR / "static"
