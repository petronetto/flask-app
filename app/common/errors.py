
"""Application error handlers."""

from wtforms.validators import ValidationError
from flask import Blueprint, jsonify, make_response
from mongoengine.errors import DoesNotExist
from werkzeug.exceptions import MethodNotAllowed

errors = Blueprint('errors', __name__)

# Generic error
@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
    if error.__class__.__name__ is not None:
        message = [str(x) for x in error.args]
        response = {
            'error': {
                'type': error.__class__.__name__,
                'message': message
            }
        }
        return make_response(jsonify(response), 400)
    if error.__class__.__name__ is None:
        response = {
            'error': {
                'type': 'UnexpectedException',
                'message': 'An unexpected error has occurred.'
            }
        }
        return make_response(jsonify(response), 500)

# Validations errors
@errors.app_errorhandler(ValidationError)
def handle_validation_errors(error):
    response = {
        'error': {
            'type': error.__class__.__name__,
            'message': error.args
        }
    }
    return make_response(jsonify(response), 422)

# Method not allowed
@errors.app_errorhandler(MethodNotAllowed)
def handle_method_not_allowed(error):
    response = {
        'error': {
            'type': 'MethodNotAllowed',
            'message': 'The method is not allowed for the requested URL'
        }
    }
    return make_response(jsonify(response), 405)

# Resource does not exists
@errors.app_errorhandler(DoesNotExist)
def handle_does_not_exist(error):
    response = {
        'error': {
            'type': error.__class__.__name__,
            'message': error.args[0]
        }
    }
    return make_response(jsonify(response), 404)
