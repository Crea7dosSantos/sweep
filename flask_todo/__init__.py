from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('flask_todo.config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import flask_todo.routes
