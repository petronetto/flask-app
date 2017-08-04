from flask_restful import Resource
from wtforms.validators import ValidationError
from app.api.common.utils import make_api_response
from .model import User, user_schema, users_schema
from .forms import CreateUserForm, UpdateUserForm

class GetUser(Resource):
    def get(self, user_id):
        user = User.objects.get(id=user_id)
        return make_api_response(user_schema, user)

class GetUsers(Resource):
    def get(self):
        users = User.objects.all()
        return make_api_response(users_schema, users)

class CreateUsers(Resource):
    def post(self):
        form = CreateUserForm()
        if form.validate_on_submit():
            user = User(
                username   = form.username.data,
                password   = form.password.data,
                email      = form.email.data,
                first_name = form.first_name.data,
                last_name  = form.last_name.data,
            )
            user.save()
            return make_api_response(user_schema, user, 201)
        raise ValidationError(form.errors)

class UpdateUser(Resource):
    def put(self, user_id):
        user = User.objects.get(id=user_id)
        form = UpdateUserForm()
        if form.validate_on_submit():
            user.update(
                username   = form.username.data,
                email      = form.email.data,
                first_name = form.first_name.data,
                last_name  = form.last_name.data,
            )
            return make_api_response(user_schema, user)
        raise ValidationError(form.errors)
