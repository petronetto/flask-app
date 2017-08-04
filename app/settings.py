import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY   = os.environ.get("SECRET_KEY")
DEBUG        = os.environ.get("DEBUG")
MONGODB_DB   = os.environ.get("MONGODB_DB")
MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_PORT = os.environ.get("MONGODB_PORT")

