"""
Validate the login requests
"""
from flask_wtf import FlaskForm as Form
from wtforms import validators, StringField

class LoginForm(Form):
    """ Validate the login requests """
    username = StringField('Username', [validators.DataRequired()])
    password = StringField('Password', [validators.DataRequired()])
