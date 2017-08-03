from flask import Flask
from flask_mongoengine import MongoEngine

mongo = MongoEngine()

app = Flask(__name__)
app.config.from_pyfile('settings.py')

mongo.init_app(app)

from app.user.handlers import user_router
app.register_blueprint(user_router)

if __name__ == '__main__':
    app.run()


