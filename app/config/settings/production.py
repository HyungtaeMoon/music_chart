import sys

import requests

from .base import *

# secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

# Django 가 runserver 로 켜졌는지 확인
RUNSERVER = 'runserver' in sys.argv
DEBUG = False
# ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

# runserver 로 production 환경을 실행할 경우
if RUNSERVER:
    DEBUG = True
    # ALLOWED_HOSTS = [
    #     'localhost',
    #     '127.0.0.1',
    # ]

# 아마존에서 제공해주는 URL에 접속을 허용하는 코드
ALLOWED_HOSTS = [
    '.amazonaws.com',
]

# Health Check 도메인을 허용하는 코드
try:
    EC2_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').text
    ALLOWED_HOSTS.append(EC2_IP)
except requests.exceptions.RequestException:
    pass

WSGI_APPLICATION = 'config.wsgi.production.application'

# INSTALLED_APPS += [
#     'storages',
# ]

# DB
# DATABASES = secrets['DATABASES']

# Log
# LOG_DIR = '/var/log/django'
# if not os.path.exists(LOG_DIR):
#     LOG_DIR = os.path.join(ROOT_DIR, '.log')
#     os.makedirs(LOG_DIR, exist_ok=True)

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'formatters': {
#         'django.server': {
#             'format': '[%(asctime)s] %(message)s',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         },
#         'file_error': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'level': 'ERROR',
#             'formatter': 'django.server',
#             'backupCount': 10,
#             'filename': os.path.join(LOG_DIR, 'error.log'),
#             'maxBytes': 10485760,
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file_error'],
#             'level': 'INFO',
#             'propagate': True,
#         }
#     }
# }
