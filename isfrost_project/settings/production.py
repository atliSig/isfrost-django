"""The production environment"""
import dj_database_url
from decouple import config
from .base import *

ALLOWED_HOSTS = ['isfrost-django.herokuapp.com']
DEBUG = True

DATABASES = {
    'default' : dj_database_url.config(
        default=config('DATABASE_URL'))
}