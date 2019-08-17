import os
from os.path import join, dirname
from dotenv import load_dotenv


load_dotenv(__file__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_NAME = os.environ.get("DB_NAME")
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
SECRET_KEY = os.environ.get("SECRET_KEY")
