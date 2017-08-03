from flask import Blueprint, jsonify, request, make_response
from .models import User

user_router = Blueprint('user_router', __name__)

@user_router.route('/users', methods=['GET', 'POST'])
def user_routes():
    if request.method == 'GET':
        return get_users()
    if request.method == 'POST':
        return create_users()

def get_users():
    users = User.objects.all()
    return make_response(jsonify(users), 200)

def create_users():
    user = User(
        username   = request.json['username'],
        password   = request.json['password'],
        email      = request.json['email'],
        first_name = request.json['first_name'],
        last_name  = request.json['last_name']
    )
    user.save()
    return make_response(jsonify(user), 201)
