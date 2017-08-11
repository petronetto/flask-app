from unittest import TestCase
from mongoengine.connection import _get_db
from app.main import create_app as create_app_base
from app.api.v1.user.models import User

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

    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def create_user(self):
        user = User(
            first_name="Admin",
            last_name="User",
            username="admin",
            email="admin@example.com",
            password="test123",
        )
        user.save()
        return user
