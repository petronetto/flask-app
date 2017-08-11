import json
from app.common.tests import TestBase
from app.api.v1.user.models import User

class UserTest(TestBase):
    def test_create_user(self):
        # Create token
        with self.app_factory.app_context():
            token = self.create_token()

        # User data
        user_data = dict(
            first_name="Test",
            last_name="User",
            username="testuser",
            email="test@example.com",
            password="test123",
            confirm="test123",
        )

        # Posting a new user
        data_json = json.dumps(user_data)
        rv = self.app.post('/api/v1/users', data=data_json,
                           content_type='application/json',
                           headers={'Authorization': 'Bearer {}'.format(token)})
        assert "test@example.com" in str(rv.data)
        assert User.objects.filter(username="testuser").count() == 1

    def test_create_user_wrong_token(self):
        token = 'token'

        # User data
        user_data = dict(
            first_name="Test",
            last_name="User",
            username="testuser",
            email="test@example.com",
            password="test123",
            confirm="test123",
        )

        # Posting a new user
        data_json = json.dumps(user_data)
        rv = self.app.post('/api/v1/users', data=data_json,
                           content_type='application/json',
                           headers={'Authorization': 'Bearer {}'.format(token)})
        self.assertEqual(rv.status_code, 422)
