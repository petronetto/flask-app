from app.main import mongo

from app.helpers.common import utc_now_ts as now

class User(mongo.Document):
    username   = mongo.StringField(required=True, unique=True)
    password   = mongo.StringField(required=True)
    email      = mongo.EmailField(required=True, unique=True)
    first_name = mongo.StringField(max_length=50)
    last_name  = mongo.StringField(max_length=50)
    created    = mongo.IntField(default=now())

    meta = {
        'indexes': ['username', 'email', '-created']
    }

