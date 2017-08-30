"""
Application tests
"""
import sys
import unittest
from os.path import join, dirname, abspath
from dotenv import load_dotenv

sys.path.append(abspath(join(dirname(__file__), '..')))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# pylint: disable=W0611,C0413
from app.api.v1.auth.tests import LoginTest
from app.api.v1.user.tests import UserTest

if __name__ == '__main__':
    unittest.main()
