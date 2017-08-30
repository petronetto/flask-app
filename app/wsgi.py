"""
Bootstrap the application
"""
from os.path import join, dirname
from dotenv import load_dotenv
from .main import create_app

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = create_app()

if __name__ == '__main__':
    app.run()
