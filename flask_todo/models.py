import datetime
from flask_todo import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.datetime.utcnow)


db.create_all()
