# coding=utf-8

"""
Source App
"""

import os
import environ
# import warnings
# import dj_database_url
from pathlib import Path
from django.utils.translation import gettext_lazy as _

env = environ.Env()
environ.Env.read_env()
# warnings.simplefilter('error', DeprecationWarning)

BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=['127.0.0.1', 'localhost'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Rest Framework
    'rest_framework',
    'rest_framework.authtoken',
    
    # Application apps
    'service'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(CONTENT_DIR, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(APP_DIR, 'db_manager.cnf'),
        },
    },
    'manager': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(APP_DIR, 'db_application.cnf'),
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'NAME',
#         'USER': 'USER',
#         'PASSWORD': 'PASSWORD',
#         'HOST': 'HOST',
#         'PORT': '3306',
#     },
#     'manager':{
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'NAME',
#         'USER': 'USER',
#         'PASSWORD': 'PASSWORD',
#         'HOST': 'HOST',
#         'PORT': '3306',
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(default=env("DJANGO_DATABASE_URL")),
#     'manager': dj_database_url.config(default=env("DATABASE_URL"))
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_ROOT = os.path.join(CONTENT_DIR, 'staticfiles')
STATIC_URL = '/content/static/'

MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media')
MEDIA_URL = '/content/media/'

STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, 'assets'),
]

LOCALE_PATHS = [
    os.path.join(CONTENT_DIR, 'locale')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
