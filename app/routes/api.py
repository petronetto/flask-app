"""
Application routes
"""
from flask_restful import Api
from app.common.errors import errors
from app.api.v1.auth.handlers import Login, Refresh
from app.api.v1.user.handlers import CreateUsers, GetUser, GetUsers, UpdateUser, DeleteUser

def register_api_routes(app):
    """
    Initialize the routes
    """

    # Loading custom error handlers
    app.register_blueprint(errors)

    api = Api(app, errors=errors, prefix='/api/v1')

    # Auth routes
    api.add_resource(Login, '/login')
    api.add_resource(Refresh, '/refresh')

    # User routes
    api.add_resource(GetUser, '/users/<string:user_id>')
    api.add_resource(GetUsers, '/users')
    api.add_resource(CreateUsers, '/users')
    api.add_resource(UpdateUser, '/users/<string:user_id>')
    api.add_resource(DeleteUser, '/users/<string:user_id>')

    return None
