# http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/

from cgbs.settings.base import *
import email

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = email.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = email.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = True
LOGIN_REDIRECT_URL = '/'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}