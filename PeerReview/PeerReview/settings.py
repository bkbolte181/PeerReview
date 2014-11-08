"""
Django settings for PeerReview project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2(+vh4q025k69rj_t@@o*n*nyj_$^=e@k6j(hai2m@^eq5g^jx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'PeerReviewApp',
    'filetransfers',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'PeerReviewApp.urls'

WSGI_APPLICATION = 'PeerReview.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

'''
	This is to make sure we keep the database information secure. If you want
	to use another database, make a file called database_info.py and store it in
	the same directory as your settings file. Then you can duplicate the DATABASES
	variable there. Otherwise the system will default to a local sqlite database.
	Make sure that the database_info.py file is included in .gitignore
'''
try:
	from database_info import DATABASES
except ImportError:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [
	os.path.join(BASE_DIR, '..', 'PeerReviewApp', 'templates'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

# All possible schools
SCHOOLS = (
	'Goizueta Business School',
	'Laney Graduate School',
	'School of Law',
	'School of Medicine',
	'Nell Hodgson Woodruff School of Nursing',
	'Rollins School of Public Health',
	'Candler School of Theology',
	'College of Arts and Sciences',
	'Other',
)

# For handling file uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'PeerReviewApp', 'media')
MEDIA_URL = '/media/'

# Points at the custom user model
AUTH_USER_MODEL = 'PeerReviewApp.SiteUser'

# The default url for handling logging in. This is necessary so that views that
# require a logged in user can redirect to the correct place.
LOGIN_URL = '/login/'