from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateTodoForm(FlaskForm):
    todo_name = StringField('TodoName', validators=[
        DataRequired(),
        Length(min=3, max=30)
    ])
    add_todo_create = SubmitField('Add Todo Create')
