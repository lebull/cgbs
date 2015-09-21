# http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/

from cgbs.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

def show_toolbar(request):
        return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}

INTERNAL_IPS = ('141.129.1.98')