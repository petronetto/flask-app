""" Web Routes """
from app.web.blueprints import Home

def register_web_routes(app):
    """ Initialize Web routes """
    app.add_url_rule('/', 'home', Home.get)
