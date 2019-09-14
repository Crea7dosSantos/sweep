import flask_todo.settings as settings
import datetime


class DevelopmentConfig:

    # Flask
    DEBUG = True

    SECRET_KEY = settings.SECRET_KEY
    JWT_SECRET_KEY = settings.JWT_SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=5)
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
