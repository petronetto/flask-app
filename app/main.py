from flask import Flask
from flask_mongoengine import MongoEngine
from flask_wtf import CSRFProtect
from flask_restful import Api
from app.common.errors import errors

app = Flask(__name__)
app.config.from_pyfile('.env')
app.register_blueprint(errors)
csrf = CSRFProtect(app)

mongo = MongoEngine()
mongo.init_app(app)
api = Api(app, errors=errors)

########################################
# Routes
########################################
from .user.handler import CreateUsers, GetUser, GetUsers, UpdateUser
api.add_resource(GetUser, '/users/<string:user_id>')
api.add_resource(GetUsers, '/users')
api.add_resource(CreateUsers, '/users')
api.add_resource(UpdateUser, '/users/<string:user_id>')

########################################
# Create App
########################################
if __name__ == '__main__':
    app.run()
