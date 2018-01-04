"""The production environment"""
import dj_database_url
from decouple import config
from .base import *

ALLOWED_HOSTS = ['isfrost-django.herokuapp.com', 'www.isfrost.is']
DEBUG = False

DATABASES = {
    'default' : dj_database_url.config(
        default=config('DATABASE_URL'))
}