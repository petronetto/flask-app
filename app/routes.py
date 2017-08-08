from .api.v1.user.handler import CreateUsers, GetUser, GetUsers, UpdateUser, DeleteUser
from flask_restful import Api
from app.common.errors import errors

def init_routes(app):

    # Carregando os errors handlers customizados
    app.register_blueprint(errors)

    api = Api(app, errors=errors)

    api.add_resource(GetUser, '/users/<string:user_id>')

    api.add_resource(GetUsers, '/users')
    api.add_resource(CreateUsers, '/users')
    api.add_resource(UpdateUser, '/users/<string:user_id>')
    api.add_resource(DeleteUser, '/users/<string:user_id>')
