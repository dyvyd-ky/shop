
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['128.199.222.115', 'elytte.com', 'www.elytte.com']

STRIPE_PUB_KEY = ''
STRIPE_SECRET_KEY = ''

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'vendor_admin'
LOGOUT_REDIRECT_URL = 'frontpage'

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

SENDGRID_API_KEY=''
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'elytte'
DEFAULT_EMAIL_FROM = 'elytte.ky@gmail.com'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_SANDBOX_MODE_IN_DEBUG = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'apps.cart',
    'apps.core',
    'apps.order',
    'apps.product',
    'apps.vendor',
    'storages',
    'crispy_forms',
    'django.contrib.flatpages',
    'apps.users',
    'ckeditor',
    'ckeditor_uploader',
    'taggit',
    'django_filters',
    #allauth

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'interiorshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.product.context_processors.menu_categories',
                'apps.cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'interiorshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'elytte',
        'USER': 'elytte',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
#MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                'codesnippet',
            ]),
    },
}

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

AWS_STORAGE_BUCKET_NAME = 'elytteky'
AWS_S3_ENDPOINT_URL = 'https://elytteky.sgp1.digitaloceanspaces.com'

AWS_S3_CUSTOM_DOMAIN = 'spaces.elytte.com/elytteky'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'elytteky'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# Use AWS_S3_ENDPOINT_URL here if you haven't enabled the CDN and got a custom domain. 
#STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'static')
#STATIC_ROOT = 'static/'

#MEDIA_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'media')
#MEDIA_ROOT = 'media/'
