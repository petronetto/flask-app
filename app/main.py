from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from users.models import User

app = Flask(__name__)

app.config.from_pyfile('config.py')
mongo = MongoEngine(app)

@app.route('/user', methods=['GET'])
def create_users():
    user = User(
        username="petronetto",
        password="secret",
        email="juliano@petronetto.com.br",
        first_name="Juliano",
        last_name="Petronetto"
    )
    return jsonify({'user': user})

@app.route('/test/<int:id>', methods=['PUT'])
def test_post(id):
    return jsonify({'value': id, 'method': 'PUT', 'request': request.json})