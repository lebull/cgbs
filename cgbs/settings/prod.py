# http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/

from cgbs.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS += [".herokuapp.com"]

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()


