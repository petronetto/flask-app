from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from .routes import init_routes

def create_app(**config_overrides):
    # Criando instancia da aplicação
    app = Flask(__name__)

    # Carregando as configs
    app.config.from_pyfile('settings.py')
    app.config.update(config_overrides)

    # Setup MongoEngine
    mongo = MongoEngine()
    mongo.init_app(app)

    # Setup the Flask-JWT-Extended extension
    jwt = JWTManager()
    jwt.init_app(app)

    # Iniciando as rotas
    init_routes(app)

    return app
