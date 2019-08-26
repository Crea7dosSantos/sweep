from flask_sqlalchemy import SQLAlchemy

# create instance
db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
