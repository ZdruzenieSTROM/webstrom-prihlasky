# pylint: disable=wildcard-import,unused-wildcard-import

from os import environ

from .settings import *

SECRET_KEY = environ["DJANGO_SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = [
    "prihlasky.strom.sk",
]

CSRF_TRUSTED_ORIGINS = [
    "https://prihlasky.strom.sk",
]

STATIC_ROOT = "/static"
