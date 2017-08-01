from flask import Blueprint, jsonify, request, make_response
from user.models import User

user_router = Blueprint('user_router', __name__)

@user_router.route('/users', methods=['POST'])
def create_users():
    user = User(
        username   = request.json['username'],
        password   = request.json['password'],
        email      = request.json['email'],
        first_name = request.json['first_name'],
        last_name  = request.json['last_name']
    )
    user.save()
    return make_response(jsonify({'user': user}), 201)