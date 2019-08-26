from flask import Flask

from flask_todo.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_todo.config.Config')

    init_db(app)

    return app


app = create_app()

import flask_todo.routes
