from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_todo.settings as settings

app = Flask(__name__)

app.config['SECRET_KEY'] = settings.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
db = SQLAlchemy(app)

import flask_todo.routes

