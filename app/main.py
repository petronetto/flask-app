from flask import Flask
from flask_restful import Api
from app.common.errors import errors
from .routes import app_routes
# from .settings import APP_CONFIG

# Criando instancia da aplicação
app = Flask(__name__)

# Carregando as configs
app.config.from_pyfile('settings.py')

# Carregando os errors handlers customizados
app.register_blueprint(errors)
api = Api(app, errors=errors)

# Iniciando as rotas
for r in app_routes:
    api.add_resource(r['class'], r['route'])

# Inicializando
if __name__ == '__main__':
    app.run()
