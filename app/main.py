"""
Main file to creates an app instance
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from .database import mongo

def create_app(**config_overrides):
    """
    Create a Flask application using the app factory pattern.

    :param config_overrides: The application configs
    :return: Flask app
    """
    # App instance
    app = Flask(__name__,
                static_folder='web/static',
                template_folder='web/template',
                instance_relative_config=True)

    # Loading configs
    app.config.from_object('app.config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    app.config.update(config_overrides)

    # Setup MongoEngine
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

    # Starting routes
    from .routes.api import init_routes
    init_routes(app)

    return app
