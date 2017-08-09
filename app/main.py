from flask import Flask
from flask_jwt_extended import JWTManager
from .routes import init_routes

# Criando instancia da aplicação
app = Flask(__name__)

# Carregando as configs
app.config.from_pyfile('settings.py')

# Setup the Flask-JWT-Extended extension
JWTManager(app)

# Iniciando as rotas
init_routes(app)

# Inicializando
if __name__ == '__main__':
    app.run()
