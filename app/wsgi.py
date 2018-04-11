"""
Bootstrap the application
"""
from os import environ
from os.path import join, dirname
from .main import create_app
# from flask.helpers import get_debug_flag

# Loading env vars
dotenv_path = join(dirname(__file__), '.env')
with open(dotenv_path) as f:
    for line in f:
        if line[0] == ' ' or line[0] == '#':
            continue
        key, value = line.split('=')
        environ[key] = value.strip()

app = create_app()

if __name__ == '__main__':
    app.run()
