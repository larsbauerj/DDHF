# -*- coding: UTF-8 -*-
#
# Django settings for ddhf project.


import os

USE_L10N = True
# hvilken platform er vi på
# Foreløbig har vi datamuseum.dk, bauers ubuntuserver.
# default behandles som localhost som adresse
uname = os.uname()[1] # hostname
prodserver = "www.datamuseum.dk"
if uname == prodserver:
  DEBUG = False
else:
  DEBUG = True
TEMPLATE_DEBUG = DEBUG

# PROJECT_ROOT = '/home/bauer/dj4/DDHF/'
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__)) + "/"
ADMINS = (
  ('Lars Bauer Joergensen', 'bauerdata@gmail.com'),
)

print PROJECT_ROOT
MANAGERS = ADMINS

DATABASE_ENGINE   = 'django.db.backends.mysql' # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME     = 'db1'      # Or path to database file if using sqlite3.
DATABASE_USER     = 'db'       # Not used with sqlite3.
DATABASE_PASSWORD = '12DB34'   # Not used with sqlite3.
DATABASE_HOST     = ''       # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT     = ''       # Set to empty string for default. Not used with sqlite3.

DATABASES = {
  'default': {
    'ENGINE'   : DATABASE_ENGINE,
    'NAME'     : DATABASE_NAME,
    'USER'     : DATABASE_USER,
    'PASSWORD' : DATABASE_PASSWORD,
    'HOST'     : DATABASE_HOST,
    'PORT'     : DATABASE_PORT,
  }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Copenhagen'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'da-DK'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
if uname == prodserver:
  MEDIA_ROOT  = PROJECT_ROOT + 'pictures/'
  MEDIA_URL   = 'http://www.datamuseum.dk/static/'
elif uname  == "ubuntuserver":
  MEDIA_ROOT  = PROJECT_ROOT + 'pictures/'
  MEDIA_URL   = 'http://90.184.105.201:8000/static/'
else:
  MEDIA_ROOT  = PROJECT_ROOT + 'pictures/'
  MEDIA_URL   = 'http://90.184.105.201:8080/static/'
  MEDIA_URL   = 'http://90.184.105.201:8000/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
STATIC_URL = '/pictures/css/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7qr+1zl@-4rqxzf+jhb$-huqqv3=xi*fcujxh)&^i7bynnvaor'

# List of callables that know how to import templates from various sources.

# if uname == prodserver:
if True:
  TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
  )
else:
  TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.load_template_source',
  )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ddhf.urls'

FORMAT_MODULE_PATH = 'ddfh_data.formats'

TEMPLATE_DIRS = (
  PROJECT_ROOT + 'ddhf/django_templates',
    PROJECT_ROOT + 'templates',
    PROJECT_ROOT + 'static',
    PROJECT_ROOT + 'static/css',
  # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
  # Always use forward slashes, even on Windows.
  # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.comments',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'ddhf',
)
