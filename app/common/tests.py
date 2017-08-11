from unittest import TestCase
from mongoengine.connection import _get_db
from flask_jwt_extended import JWTManager, create_access_token
from app.main import create_app as create_app_base
from app.api.v1.user.models import User, user_schema

class TestBase(TestCase):
    def create_app(self):
        self.db_name = 'flask_test'
        return create_app_base(
            MONGODB_SETTINGS={'DB': self.db_name},
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SECRET_KEY='mySecret',
        )

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()
        with self.app_factory.app_context():
            self.jwt_manager = JWTManager(self.app_factory)


    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def get_user(self):
        return User(
            first_name="Admin",
            last_name="User",
            username="admin",
            email="admin@example.com",
            password="test123",
        )

    def create_user(self):
        user = self.get_user()
        user.save()
        return user

    def create_token(self):
        user = self.create_user()
        u = user_schema.dump(user)
        return create_access_token(identity=u.data['id'])
