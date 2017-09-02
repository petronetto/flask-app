"""
Main file to creates an app instance
"""
from flask import Flask
from .config.extensions import register_extensions
from .routes.api import register_api_routes
from .routes.web import register_web_routes

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
    register_extensions(app)

    # Starting routes
    register_api_routes(app)
    register_web_routes(app)

    return app
