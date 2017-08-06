import os
from flask_mongoengine import MongoEngine
from app.settings import MONGODB_DB, MONGODB_HOST, MONGODB_PORT

mongo = MongoEngine()

mongo.connect(
    MONGODB_DB,
    host = MONGODB_HOST,
    port = int(MONGODB_PORT)
)
