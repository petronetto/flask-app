import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=W0611,C0413
from app.api.v1.auth.tests import LoginTest
from app.api.v1.user.tests import UserTest

if __name__ == '__main__':
    unittest.main()
