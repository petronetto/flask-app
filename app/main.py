from flask import Flask
from flask_wtf import CSRFProtect
from flask_restful import Api
from app.common.errors import errors
from .routes import app_routes

# Criando instancia da aplicação
app = Flask(__name__)

# Carregando as configs
app.config.from_pyfile('settings.py')

# Desabilitando o CSRF
app.config.update(dict(
    WTF_CSRF_CHECK_DEFAULT=False,
    WTF_CSRF_ENABLED=False
))
CSRFProtect(app)

# Carregando os errors handlers customizados
app.register_blueprint(errors)
api = Api(app, errors=errors)

# Iniciando as rotas
for r in app_routes:
    api.add_resource(r['class'], r['route'])

# Inicializando
if __name__ == '__main__':
    app.run()
