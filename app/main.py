from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flasgger import Swagger
from .routes import init_routes

def create_app(**config_overrides):
    # Criando instancia da aplicação
    app = Flask(__name__)

    # Carregando as configs
    app.config.from_pyfile('settings.cfg')
    app.config.update(config_overrides)

    # Setup MongoEngine
    mongo = MongoEngine()
    mongo.init_app(app)

    # Setup the Flask-JWT-Extended extension
    jwt = JWTManager()
    jwt.init_app(app)

    # Setup Swagger
    template = {
        "swagger": "2.0",
        "info": {
            "title": "My Flask API",
            "description": "API for my data",
            "contact": {
                "responsibleOrganization": "ME",
                "responsibleDeveloper": "Me",
                "email": "me@me.com",
                "url": "www.me.com",
            },
            "termsOfService": "http://me.com/terms",
            "version": "0.0.1"
        },
        "schemes": [
            "http",
            "https"
        ],
        "operationId": "getmyData"
    }
    swagger = Swagger(template=template)
    swagger.init_app(app)

    # Iniciando as rotas
    init_routes(app)

    return app
