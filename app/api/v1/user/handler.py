from flask_restful import Resource
from flask_jwt_extended import jwt_required
from wtforms.validators import ValidationError
from app.api.common.utils import make_api_response
from app.helpers.utils import utc_now_ts as now
from .model import User, user_schema, users_schema
from .forms import CreateUserForm, UpdateUserForm

class GetUser(Resource):
    @jwt_required
    def get(self, user_id):
        user = User.objects.get_or_404(id=user_id)
        return make_api_response(user_schema, user)

class GetUsers(Resource):
    @jwt_required
    def get(self):
        users = User.objects.all()
        return make_api_response(users_schema, users)

class CreateUsers(Resource):
    @jwt_required
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
    @jwt_required
    def put(self, user_id):
        user = User.objects.get_or_404(id=user_id)
        form = UpdateUserForm()
        if form.validate_on_submit():
            user.username   = form.username.data
            user.email      = form.email.data
            user.first_name = form.first_name.data
            user.last_name  = form.last_name.data
            user.updated_at = now()
            user.save()
            return make_api_response(user_schema, user)
        raise ValidationError(form.errors)

class DeleteUser(Resource):
    @jwt_required
    def delete(self, user_id):
        user = User.objects.get_or_404(id=user_id)
        user.delete()
        return make_api_response(user_schema, user, 204)
