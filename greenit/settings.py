'''
Django settings for greenit project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
'''

from datetime import timedelta
import os
from pathlib import Path

import sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if config('DEBUG') == 'False' else True

ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                 'api.greenitcommunity.com', '0.0.0.0', '13.38.18.186', '*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_filters',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'graphql_auth',
    'corsheaders',
    'django_admin_json_editor',
    'storages',
    'ingredient',
    'recipe',
    'comment',
    'tag',
    'anymail',
    'translation',
    'user',
    'utensil',
    'newsletter',
    'greenit'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# just for development
if DEBUG == True:
    CORS_ALLOW_ALL_ORIGINS = True

GRAPHENE = {
    'SCHEMA': 'greenit.schema.schema',
    'MIDDLEWARE': ['graphene_django.debug.DjangoDebugMiddleware',         'graphql_jwt.middleware.JSONWebTokenMiddleware',
                   ],
}

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
    'graphql_auth.backends.GraphQLAuthBackend',
]

############### Configuration for AUTH ###############

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_EXPIRATION_DELTA": timedelta(minutes=10),
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
    ],
    # optional
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,

}

GRAPHQL_AUTH = {
    'ALLOW_LOGIN_NOT_VERIFIED': False,
    "EMAIL_TEMPLATE_VARIABLES": {
        "protocol": os.getenv('PROTOCOL'),
        "site_name": "Greenit",
        "domain": os.getenv('DOMAIN_NAME'),
        "path": "activate"
    },
    "REGISTER_MUTATION_FIELDS": ["email", "username",
                                 "user_category_lvl",
                                 "user_want_from_greenit",
                                 "user_category_age", "is_follow_newsletter"],
    "UPDATE_MUTATION_FIELDS": ["image_profile"],
}

GRAPHQL_JWT = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'ALLOW_LOGIN_NOT_VERIFIED': False,
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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
############### DATABASE ###############

ROOT_URLCONF = 'greenit.urls'

WSGI_APPLICATION = 'greenit.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_DB_NAME', "greenit"),
        'USER': config('POSTGRES_DB_USER', "user"),
        'PASSWORD': config('POSTGRES_DB_PASS', "password"),
        'HOST': config('POSTGRES_DB_HOST', "localhost"),
        "PORT": os.environ.get("POSTGRES_DB_PORT", "5432"),
        "ATOMIC_MUTATIONS": True, # need to do this only for important transaction --> bad performance
    }
}

# aws settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_S3_FILE_OVERRIDE = False

# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'greenit.storage_backends.PublicMediaStorage'


AUTH_USER_MODEL = 'user.User'

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_USE_TLS = True

# Faire une vairable
ANYMAIL = {
    "MAILJET_API_KEY": config('MAILJET_API_KEY'),
    "MAILJET_SECRET_KEY": config('MAILJET_SECRET_KEY'),
    "MAILGUN_SENDER_DOMAIN": 'localhost',  # your Mailgun domain, if needed
}

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

if DEBUG == False:
    sentry_sdk.init(
        dsn=config("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        attach_stacktrace=True,
        traces_sample_rate=1.0,
    )

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CAPTCHA_SECRET_KEY = config('CAPTCHA_SECRET_KEY')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static_file_django/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
CORS_ORIGIN_ALLOW_ALL = True
