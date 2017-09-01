"""
Provides a basic auth decorator
"""
from functools import wraps
from werkzeug.exceptions import Unauthorized
from flask import request
from app.api.v1.user.models import User
from app.common.utils import check_password

def check_auth(username, password):
    """
    This function is called to check if a username
    password combination is valid.
    """
    user = User.objects(username=username).first()
    if user and check_password(user.password, password):
        return True
    return False

def requires_auth(f):
    """ Decoretorn to check user auth """
    @wraps(f)
    def decorated(*args, **kwargs):
        """ Check user auth """
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            raise Unauthorized('Could not verify your access level for that URL.'
                               'You have to login with proper credentials')
        return f(*args, **kwargs)
    return decorated
