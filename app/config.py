# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = True

# Application root
# APPLICATION_ROOT = '/api/v1'
# URL_PREFIX = '/api/v1'

# Environment
APP_SETTINGS="development"

# Flask bootstrap
FLASK_APP="main.py"

# Secret key
SECRET="w46eM4Gyy@BgBtUCt3tM#lIljF$pcAn7pPW0BJ%c1bC73Cgw!Nis4b5kAoTQbQuAi"

# Define the database 
MONGO_DBNAME="flask_app"
MONGO_URI = 'mongodb://0.0.0.0:27017/database'
