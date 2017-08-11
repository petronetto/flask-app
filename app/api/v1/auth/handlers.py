from app.api.v1.user.models import User, user_schema
from app.helpers.utils import check_password
from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_restful import Resource
from wtforms.validators import ValidationError
from werkzeug.exceptions import Unauthorized
from .forms import LoginForm

class Login(Resource):
    def post(self):
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
    def post(self):
        current_user = get_jwt_identity()
        token = {
            'access_token': create_access_token(identity=current_user)
        }
        return make_response(jsonify(token), 200)
