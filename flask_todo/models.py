from datetime import datetime
from flask_todo import db, ma


class Todo(db.Model):

    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    user_id = db.Column(db.Integer, nullable=False)


class TodoSchema(ma.ModelSchema):
    class Meta:
        model = Todo


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(120), nullable=True)
    profile_back_image = db.Column(db.String(120), nullable=True
                                   )


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
