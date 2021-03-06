"""
User model
"""
from app.common.utils import utc_now_ts as now, hash_password, format_date
from app.config.extensions import mongo
from marshmallow import Schema, fields
from mongoengine import signals

class User(mongo.Document):
    """ User model """
    # pylint: disable=E1101
    username   = mongo.StringField(required=True, unique=True)
    password   = mongo.StringField(required=True)
    email      = mongo.EmailField(required=True, unique=True)
    first_name = mongo.StringField(max_length=50)
    last_name  = mongo.StringField(max_length=50)
    created_at = mongo.IntField(default=now())
    updated_at = mongo.IntField(default=now())
    # pylint: enable=E1101

    @classmethod
    # pylint: disable=W0613
    def pre_save(cls, sender, document, **kwargs):
        """
        Before save, lower case the username, enail
        and hash the password
        """
        # pylint: enable=W0613
        document.username = document.username.lower()
        document.email    = document.email.lower()
        document.password = hash_password(document.password)

    meta = {
        'indexes': ['username', 'email', '-created_at']
    }

# Rodar os métodos antes de salvar
signals.pre_save.connect(User.pre_save, sender=User)

class UserSchema(Schema):
    """ User Schema """
    class Meta(object):
        """ Display data ordered """
        ordered=True

    id         = fields.Str()
    username   = fields.Str()
    email      = fields.Str()
    first_name = fields.Str()
    last_name  = fields.Str()
    created_at = fields.Method('format_created_at')
    updated_at = fields.Method('format_updated_at')

    def format_created_at(self, obj):
        """ Format the date """
        return format_date(obj.created_at, '%Y-%m-%d %H:%M:%S')

    def format_updated_at(self, obj):
        """ Format the date """
        return format_date(obj.updated_at, '%Y-%m-%d %H:%M:%S')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
