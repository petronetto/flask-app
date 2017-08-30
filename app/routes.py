"""
Application routes
"""

def init_routes(app):
    """
    Initialize the routes
    """
    from flask_restful import Api
    # Loading custom error handlers
    from app.common.errors import errors
    app.register_blueprint(errors)

    api = Api(app, errors=errors, prefix='/api/v1')

    # Auth routes
    from app.api.v1.auth.handlers import Login, Refresh
    api.add_resource(Login, '/login')
    api.add_resource(Refresh, '/refresh')

    # User routes
    from app.api.v1.user.handlers import CreateUsers, GetUser, GetUsers, UpdateUser, DeleteUser
    api.add_resource(GetUser, '/users/<string:user_id>')
    api.add_resource(GetUsers, '/users')
    api.add_resource(CreateUsers, '/users')
    api.add_resource(UpdateUser, '/users/<string:user_id>')
    api.add_resource(DeleteUser, '/users/<string:user_id>')
