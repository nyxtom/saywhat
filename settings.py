import os
import sys

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

# Media/static file related paths + urls
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'uploads/')
MEDIA_URL = os.path.join(STATIC_URL, 'uploads/')
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2^!=6!&@=)9_k$0q$e5bc_6t(d3riizgsm^-3&(e)2r9dby9e4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Add the apps directory to the first position of the PYTHON_PATH, but keeping our dir in the top too
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../'))
sys.path.insert(1, os.path.join(PROJECT_ROOT, 'apps'))

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'utils',
    'djcelery',
    'south',
    'live',
    'main',
)

# Celery/Redis configuration settings
BROKER_BACKEND = "redis"
BROKER_HOST = "localhost"
BROKER_PORT = 6379
BROKER_VHOST = "0"
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
CELERY_SEND_EVENTS = True
CELERY_RESULT_BACKEND = "redis"

CELERY_DISABLE_RATE_LIMITS = True
CELERY_IGNORE_RESULT = True
CELERY_ACKS_LATE = True
CELERYD_ETA_SCHEDULER_PRECISION = 0.1

import djcelery
djcelery.setup_loader()

# Session backend to redis
SESSION_ENGINE = 'utils.sessions.backends.redis_backend'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
white="\033[1;37m"
nc="\033[0m"
try:
    from local_settings import *
    INSTALLED_APPS += EXTRA_INSTALLED_APPS
    MIDDLEWARE_CLASSES += EXTRA_MIDDLEWARE_CLASSES
except ImportError:
    print red + """
    You need to create a local_settings.py file which needs to contain at least
    database connection information.
    """ + nc
    import sys
    sys.exit(1)
