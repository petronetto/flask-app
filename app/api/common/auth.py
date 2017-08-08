from app.api.v1.user.model import User, user_schema
from app.helpers.utils import check_password
from werkzeug.exceptions import Unauthorized

def authenticate(username, password):
    user = User.objects(username=username).first()
    if user and check_password(user.password, password):
        return user
    raise Unauthorized('Invalid e-mail and/or password')

def identity(payload):
    user_id = payload['identity']
    return User.objects(id=user_id).first()
