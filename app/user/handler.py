from flask import jsonify, make_response
from flask_restful import Resource
from wtforms.validators import ValidationError
from .model import User
from .forms import CreateUserForm

class GetUser(Resource):
    def get(self, user_id):
        user = User.objects.get(id=user_id)
        return make_response(jsonify(user), 200)

class GetUsers(Resource):
    def get(self):
        users = User.objects.all()
        return make_response(jsonify(users), 200)

class CreateUsers(Resource):
    def post(self):
        form = CreateUserForm(csrf_enabled=False)
        if form.validate_on_submit():
            user = User(
                username   = form.username.data,
                password   = form.password.data,
                email      = form.email.data,
                first_name = form.first_name.data,
                last_name  = form.last_name.data,
            )
            return make_response(jsonify(user), 201)
        raise ValidationError(form.errors)

class UpdateUser(Resource):
    def get(self, user_id):
        user = User.objects.get(id=user_id)
        return make_response(jsonify(user), 200)