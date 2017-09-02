from flask_mongoengine import MongoEngine
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect
from .settings import SWAGGER_TEMPLATE

mongo   = MongoEngine()
jwt     = JWTManager()
csrf    = CSRFProtect()
swagger = Swagger(template=SWAGGER_TEMPLATE)

def register_extensions(app):
    """Register Flask extensions."""
    mongo.init_app(app)
    jwt.init_app(app)
    csrf.init_app(app)
    swagger.init_app(app)
    return None
