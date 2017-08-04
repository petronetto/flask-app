import re
from flask import request
from flask_wtf import FlaskForm as Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError

from .model import User

class BaseUserForm(Form):
    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])
    email = EmailField('Email address', [
        validators.DataRequired(),
        validators.Email()
        ])

    username = StringField('Username', [
        validators.DataRequired(),
        validators.length(min=4, max=25)
        ])
    confirm = PasswordField('Repeat Password')

class PasswordBaseForm(Form):
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.length(min=4, max=80)
        ])

class CreateUserForm(BaseUserForm, PasswordBaseForm):
    def validate_username(form, field):
        if User.objects.filter(username=field.data).first():
            raise ValidationError("Username already exists")
        if not re.match("^[a-zA-Z0-9_-]{4,25}$", field.data):
            raise ValidationError("Invalid username")

    def validate_email(form, field):
        if User.objects.filter(email=field.data).first():
            raise ValidationError("Email is already in use")

class UpdateUserForm(BaseUserForm):
    def validate_username(form, field):
        user = User.objects.filter(username=field.data).first()
        user_id = request.url.rsplit('/', 1)[-1]
        if user and user_id != str(user.id):
            raise ValidationError('Username already exists')
        if not re.match("^[a-zA-Z0-9_-]{4,25}$", field.data):
            raise ValidationError("Invalid username")

    def validate_email(form, field):
        user = User.objects.filter(email=field.data).first()
        user_id = request.url.rsplit('/', 1)[-1]
        if user and user_id != str(user.id):
            raise ValidationError("Email is already in use")
