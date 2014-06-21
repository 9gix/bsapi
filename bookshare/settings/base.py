"""
Django settings for bookshare project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# The directory for assets which are served to users.
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nns%#=gj+u6s9819h9si&zrqvv9k8@6u%aq-904dh1p)nfh6g8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    ###################
    # PRE INSTALL APP #
    ###################


    ######################
    # Django Contrib App #
    ######################
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    ###################
    # Third Party App #
    ###################
    'corsheaders',
    #'debug_toolbar.apps.DebugToolbarConfig', # for django>=1.7
    'django_extensions',
    'haystack',
    'oauth2_provider',
    'rest_framework',
    'social.apps.django_app.default',


    ################
    # Internal App #
    ################
    'accounts',
    'catalog',
    'comm',
    'communities',
    'ownership',

    ####################
    # POST INSTALL APP #
    ####################


)


MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bookshare.urls'

WSGI_APPLICATION = 'bookshare.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images, client app template)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# User Uploaded Media File (pdf, image, doc, etc. )
MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')
MEDIA_URL = '/media/'

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'PAGINATE_BY': 20
}

# HTML Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Template Context
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "bookshare.context_processors.site",

)


# Authentication (django.contrib.auth, accounts, or similar apps)
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'

# Site Framework
SITE_ID = 1

# Fixture Directory (Initial Data, Dump Data, Test Data, etc.)
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

# Distributed Task
BROKER_URL = "amqp://guest:guest@localhost:5672//"
CELERY_RESULT_BACKEND = 'amqp://'

# CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:9000',
    'localhost:9000',
)

# Search API
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
    'advanced': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'bookshare',
    }
}

# Shell Plus
SHELL_PLUS = "ipython"

SHELL_PLUS_PRE_IMPORTS = (
)

SHELL_PLUS_POST_IMPORTS = (
    ('catalog.serializers', '*'),
    ('catalog.views', '*'),
    ('pprint','pprint'),
    ('urllib', 'request'),
)
