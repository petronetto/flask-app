import json
from app.common.tests import TestBase

class LoginTest(TestBase):
    def test_login_user(self):
        # create user
        self.create_user()

        # loging with user
        data_json = json.dumps(dict(username='admin', password='test123'))
        rv = self.app.post('/api/v1/login', data=data_json, content_type='application/json')
        assert "access_token" in str(rv.data)

    def test_login_user_wrong_pass(self):
        # create user
        self.create_user()

        # loging with user
        data_json = json.dumps(dict(username='admin', password='test1234'))
        rv = self.app.post('/api/v1/login', data=data_json, content_type='application/json')
        assert "access_token" not in str(rv.data)
