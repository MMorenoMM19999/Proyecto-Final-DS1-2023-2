# -*- encoding: utf-8 -*-
"""
Django settings for concesionario project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l^bwzdk8(+z(k31v0^p@vtw!a3qb40n#0wf%z4uy5ix2p#z^kl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Send email for forgotten passwords
# Is necesary configure your account to allow django use it to send mails
# put allow insecure apps turn on in your google account (it puts your account vulnerable)

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 25 #Raises an error that I can not solve yet (SMTP AUTH extension not supported by server)
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'aureliowebpages@gmail.com'
#EMAIL_HOST_PASSWORD = '1143843823'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Para utilizar imagekit
    'imagekit',
    # Para dar estilos usando bootstrap a los campos de los formularios
    'bootstrap3',
    'django.contrib.humanize',
    # para el pdf
    'easy_pdf',
    # Apps
    # Administra el inicio y cierre de sesion
    'apps.inicio',
    # Administra la presentacion de los perfiles de cada usuario
    'apps.cuenta',
    # Administra el crud del empleado
    'apps.empleado',
    # Administra el crud de la sucursal
    'apps.sucursal',
    # Administra el crud de vehiculo
    'apps.vehiculo',
    # Administrad el crud de repuesto
    'apps.repuesto',
    # Administra el crud de cliente
    'apps.cliente',
    # Administrad el crud de orden de trabajo
    'apps.orden_de_trabajo',
    'apps.cotizacion_orden_de_trabajo',
    'apps.factura_orden_de_trabajo',
    # Administra el crud de venta
    'apps.venta',
    # Administra el crud de cotizacion
    'apps.cotizacion',
    # Administra el crud de proveedores
    'apps.proveedor',
    'apps.reporte',
    'apps.movil',
    'corsheaders',
)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]


ROOT_URLCONF = 'concesionario.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # This option allow to use the MEDIA_URL in templates
                # 'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'concesionario.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'concesionariobd2',  # Remove the extra space at the end
        'USER': 'postgres',  # SAME AS sqlshell username
        'PASSWORD': 'kevin1234',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# Idioma castellano
LANGUAGE_CODE = 'es'
# Idioma ingles
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# MEDIA_URL = 'http://localhost:8000/media/'
MEDIA_URL = '/media/'

# Humanize settings
USE_THOUSAND_SEPARATOR = True

# http://stackoverflow.com/questions/22476273/no-access-control-allow-origin-header-is-present-on-the-requested-resource-i
CORS_ORIGIN_ALLOW_ALL = True
