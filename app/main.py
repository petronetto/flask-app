from flask import Flask
from .routes import init_routes
from app.api.common.auth import authenticate, identity
from flask_jwt import JWT

# Criando instancia da aplicação
app = Flask(__name__)

# Carregando as configs
app.config.from_pyfile('settings.py')

JWT(app, authenticate, identity)

# Iniciando as rotas
init_routes(app)

# Inicializando
if __name__ == '__main__':
    app.run()
