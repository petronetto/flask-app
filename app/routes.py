from flask_restful import Api
from app.common.errors import errors
from app.api.v1.user.handlers import CreateUsers, GetUser, GetUsers, UpdateUser, DeleteUser
from app.api.v1.auth.handlers import Login, Refresh

def init_routes(app):

    # Carregando os errors handlers customizados
    app.register_blueprint(errors)

    api = Api(app, errors=errors, prefix='/api/v1')

    api.add_resource(Login, '/login')
    api.add_resource(Refresh, '/refresh')

    api.add_resource(GetUser, '/users/<string:user_id>')

    api.add_resource(GetUsers, '/users')
    api.add_resource(CreateUsers, '/users')
    api.add_resource(UpdateUser, '/users/<string:user_id>')
    api.add_resource(DeleteUser, '/users/<string:user_id>')
