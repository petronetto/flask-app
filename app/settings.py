"""
Load application configs vars
"""
from os import environ as env
print('Loading environment variables')

SECRET_KEY             = env.get('SECRET_KEY')
MONGODB_DB             = env.get('MONGODB_DB')
MONGODB_HOST           = env.get('MONGODB_HOST')
MONGODB_PORT           = int(env.get('MONGODB_PORT'))
DEBUG                  = True
WTF_CSRF_CHECK_DEFAULT = False
WTF_CSRF_ENABLED       = False
JSON_SORT_KEYS         = False
