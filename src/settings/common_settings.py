"""
Django settings for the CSV import project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
import os
from os.path import dirname, realpath, join
from sys import path

BASE_DIR = dirname(dirname(dirname(realpath(__file__))))

location = lambda x: join(dirname(dirname(realpath(__file__))), x)

path.append(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'djangobower',
    'django_nose',
    'djangojs',
    'src.apps.hotel'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.setdefault("DB_NAME", ""),
        'USER': os.environ.setdefault("DB_USER", ""),
        'PASSWORD': os.environ.setdefault("DB_PASSWORD", ""),
        'HOST': os.environ.setdefault("DB_HOST", ""),
        'PORT': os.environ.setdefault("DB_PORT", ""),
        'ATOMIC_REQUESTS': True,
    }
}

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'src.urls'

WSGI_APPLICATION = 'src.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Logging
# see https://docs.djangoproject.com/en/1.7/topics/logging/#configuring-logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'application_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.environ.setdefault("DJANGO_APPLICATION_LOG", "log/application.log"),
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'application_log'],
        },
        'django.request': {
            'handlers': ['mail_admins', 'application_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins', 'application_log'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console', 'application_log'],
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

STATIC_ROOT = location('public/static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

STATICFILES_DIRS = (
    location('static'),
)

MEDIA_ROOT = os.environ.setdefault("MEDIA_ROOT", "")

MEDIA_URL = os.environ.setdefault("MEDIA_URL", "")

TEMPLATE_DIRS = (
    location('templates'),
)

# bower settings
BOWER_COMPONENTS_ROOT = join(BASE_DIR, 'bower_components')

BOWER_INSTALLED_APPS = (
    'bootstrap',
    'jquery',
    'typeahead.js',
    'underscore',
)

# Testing configuration
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Nose settings
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=src/apps/hotel',
]

# Import data
IMPORT_DATASOURCE_DIR = join(BASE_DIR, 'data')
