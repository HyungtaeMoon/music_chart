import sys

import requests

from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

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
DATABASES = secrets['DATABASES']

# AWS SNS
EMAIL_HOST = secrets['EMAIL_HOST']
EMAIL_HOST_USER = secrets['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = secrets['EMAIL_HOST_PASSWORD']
EMAIL_PORT = secrets['EMAIL_PORT']
