"""
Load application configs vars
"""
from os import environ as env

SECRET_KEY             = env.get('SECRET_KEY', 'super-secret-key')
MONGODB_DB             = env.get('MONGODB_DB', 'flask')
MONGODB_HOST           = env.get('MONGODB_HOST', '0.0.0.0')
MONGODB_PORT           = int(env.get('MONGODB_PORT', '27017'))
DEBUG                  = True
WTF_CSRF_CHECK_DEFAULT = False
WTF_CSRF_ENABLED       = False
JSON_SORT_KEYS         = False
WEBPACK_MANIFEST_PATH  = 'web/webpack/manifest.json'

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "My Flask API",
        "description": "API for my data",
        "contact": {
            "responsibleOrganization": "ME",
            "responsibleDeveloper": "Me",
            "email": "me@me.com",
            "url": "www.me.com",
        },
        "termsOfService": "http://me.com/terms",
        "version": "0.0.1"
    },
    "schemes": [
        "http",
        "https"
    ],
    "operationId": "getmyData"
}
