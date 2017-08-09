from app.api.v1.user.model import User, user_schema
from app.helpers.utils import check_password
from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, \
     jwt_refresh_token_required, get_jwt_identity
from flask_restful import Resource
from werkzeug.exceptions import Unauthorized

class Login(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']
        user = User.objects(username=username).first()
        if user and check_password(user.password, password):
            u = user_schema.dump(user)
            token = {
                'access_token': create_access_token(identity=u.data),
                'refresh_token': create_refresh_token(identity=u.data)
            }
            return make_response(jsonify(token), 200)
        raise Unauthorized('Invalid credentials')

class Refresh(Resource):
    def post(self):
        current_user = get_jwt_identity()
        token = {
            'access_token': create_access_token(identity=current_user)
        }
        return make_response(jsonify(token), 200)
