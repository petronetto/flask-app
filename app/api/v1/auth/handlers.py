"""
Handle with HTTP requests for auth routes
"""
from app.api.v1.user.models import User, user_schema
from app.common.utils import check_password
from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_restful import Resource
from flasgger import swag_from
from wtforms.validators import ValidationError
from werkzeug.exceptions import Unauthorized
from .forms import LoginForm

class Login(Resource):
    """
    Handle with login request
    """
    @swag_from('login.yml')
    def post(self):
        """ Returns a JWT token to user """
        form = LoginForm()
        if form.validate_on_submit():
            username = request.json['username']
            password = request.json['password']
            user = User.objects(username=username).first()
            if user and check_password(user.password, password):
                u = user_schema.dump(user)
                token = {
                    'access_token': create_access_token(identity=u.data['id'])
                }
                return make_response(jsonify(token), 200)
            raise Unauthorized('Invalid credentials')
        raise ValidationError(form.errors)

class Refresh(Resource):
    """
    Handle with refresh token request
    """
    def post(self):
        """ Returns a refreshed token to user """
        current_user = get_jwt_identity()
        token = {
            'access_token': create_access_token(identity=current_user)
        }
        return make_response(jsonify(token), 200)
