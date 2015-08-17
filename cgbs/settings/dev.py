# http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/

from cgbs.settings.base import *
import email

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
