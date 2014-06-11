"""
Django settings for manejalo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iirxm_5*uas^3w=eu3b(m7%j3y%bvz05cvs0#6ix+8-5sl+e&v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'widget_tweaks',
    'form_utils',
    'tastypie',
    'haystack',
    'usuarios',
    'demografia',
    'app',
    'anuncio',
    'south',
    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'manejalo.urls'

WSGI_APPLICATION = 'manejalo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data.db'),
    }
}

TEMPLATE_DIRS = (
    (os.path.join(os.path.dirname(__file__), '../templates'),)
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-CL'

TIME_ZONE = 'Chile/Continental'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



STATICFILES_DIRS = (
    os.path.join( BASE_DIR, "static" ),
)



#MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../uploaded-content')
#MEDIA_URL = 'http://localhost:8000/media/'

MEDIA_ROOT = '/media/'
STATIC_ROOT = '/static/'

AUTH_USER_MODEL = 'usuarios.Usuario'


HAYSTACK_CONNECTIONS  =  { 
    'default' :  { 
        'ENGINE' :  'haystack.backends.solr_backend.SolrEngine' , 
        'URL' :  'http://127.0.0.1:8983/solr' 
        # ... O para multicore ... 
        # 'URL': 'http://127.0.0.1:8983/solr/mysite', 
    }, 
}

# AWS_ACCESS_KEY_ID = 'AKIAJ6DIYIC23QVFHQHA'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'manejalo'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# STATIC_URL = S3_URL


STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

TASTYPIE_DEFAULT_FORMATS = ['json']