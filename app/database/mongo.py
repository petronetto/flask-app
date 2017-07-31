from flask_mongoengine import MongoEngine
from server import app

mongo = MongoEngine(app)
