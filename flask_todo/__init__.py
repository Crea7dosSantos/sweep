from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config.from_object('flask_todo.config.Config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

import flask_todo.routes
