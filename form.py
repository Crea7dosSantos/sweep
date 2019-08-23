from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length


class CreateTodoForm(FlaskForm):
    todo_name = StringField('TodoName', validators=[
        DataRequired(),
        Length(min=3, max=50)
    ])
    add_todo_create = SubmitField('Add Todo Create')


class SignUpForm(FlaskForm):
    user_name = StringField('Username', validators=[
        DataRequired(),
        Length(min=4, max=20)
    ])
    user_email = StringField('Email Address', validators=[
        DataRequired(),
        Length(min=6, max=40)
    ])
    user_password = PasswordField('Password', validators=[
        DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    auth_button = SubmitField('Sign Up')


class LoginForm(SignUpForm):
    auth_button = SubmitField('Login')
