from flask import Flask
from flask_mongoengine import MongoEngine

mongo = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    mongo.init_app(app)

    from user.handlers import user_router
    app.register_blueprint(user_router)

    return app