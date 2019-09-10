import flask_todo.settings as settings


class DevelopmentConfig:

    # Flask
    DEBUG = True

    SECRET_KEY = settings.SECRET_KEY
    JWT_SECRET_KEY = settings.JWT_SECRET_KEY
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
