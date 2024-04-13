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
