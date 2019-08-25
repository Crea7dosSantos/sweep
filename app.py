from flask import Flask, redirect, render_template, request, url_for
import setting
from form import CreateTodoForm, LoginForm, SignUpForm
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = setting.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8'.format(**{
    'user': setting.USER_NAME,
    'password': setting.PASSWORD,
    'host': setting.HOST_NAME,
    'db': setting.DB_NAME
})
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    title = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.datetime.utcnow)


db.create_all()


@app.route('/', methods=['GET', 'POST'])
@app.route('/create', methods=['GET', 'POST'])
def index():
    form = CreateTodoForm()
    if form.validate_on_submit():
        input_form_data = request.form['todo_name']
        todo = Todo(title=input_form_data)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))

    todos = db.session.query(Todo).all()
    return render_template('index.html', form=form, todos=todos)


@app.route('/<int:id>delete', methods=('POST',))
def delete(id):
    db.session.query(Todo).filter(Todo.id == id).delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        pass
    return render_template('signup.html', form=form)


app.run(debug=True)
