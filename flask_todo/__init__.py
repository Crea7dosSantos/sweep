from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_todo.config.Config')

db = SQLAlchemy(app)

import flask_todo.routes
