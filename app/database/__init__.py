import os
import mongoengine as mongo
from app.settings import MONGODB_DB, MONGODB_HOST, MONGODB_PORT

mongo.connect(
    MONGODB_DB,
    host = MONGODB_HOST,
    port = int(MONGODB_PORT)
)
