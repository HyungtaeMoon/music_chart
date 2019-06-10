from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True

# WSGI
WSGI_APPLICATION = 'config.wsgi.dev.application'

# DB
# DATABASES = secrets['DATABASES']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# django-storages
# INSTALLED_APPS += [
#     'storages',
# ]

# Media
# AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
