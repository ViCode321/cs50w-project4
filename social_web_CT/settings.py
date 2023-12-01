"""
Django settings for social_web_CT project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ts4d^rky2nujh4-2sk8lgt4_k^roht9%d4xwpid_+u2rg9fbuf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
AUTH_USER_MODEL = 'app.CustomUser'
ALLOWED_HOSTS = []
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SESSION_ENGINE = "django.contrib.sessions.backends.db"
API_KEY = "afcfd6b34e8710d8c491b85857b75ecc"

# Configuración para enviar correos electrónicos
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


# Application definition

INSTALLED_APPS = [
    'app.apps.OrdersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.ActiveUserMiddleware',
]

ROOT_URLCONF = 'social_web_CT.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'social_web_CT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4,
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es'  # Establece el idioma por defecto en español

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Configuración de idiomas permitidos
LANGUAGES = [
    ('es', _('Spanish')),  # Añade 'es' a la lista de idiomas permitidos
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Ruta a los archivos de traducción
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images/')

# Configuración adicional para imágenes de perfil
PROFILE_PICS_DIR = 'profile_pics/'  # Ruta relativa a MEDIA_ROOT
PROFILE_PICS_ROOT = os.path.join(MEDIA_ROOT, PROFILE_PICS_DIR)
PROFILE_PICS_URL = os.path.join(MEDIA_URL, PROFILE_PICS_DIR)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
