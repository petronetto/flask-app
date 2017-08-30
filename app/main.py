"""
Main file to creates an app instance
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from .database import mongo

def create_app(**config_overrides):
    """
    Creates an app instance
    """
    # App instance
    app = Flask(__name__)

    # Loading configs
    app.config.from_pyfile('settings.py')
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
    from .routes import init_routes
    init_routes(app)

    return app
