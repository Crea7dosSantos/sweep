from flask import render_template, url_for, redirect, request, jsonify
from flask_todo import app, db
from flask_todo.form import CreateTodoForm, LoginForm, SignUpForm
from flask_todo.models import Todo, TodoSchema


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
    # return render_template('index.html', form=form, todos=todos)
    return jsonify({'status': 'ok',
                    'todos': TodoSchema(many=True).dump(todos)})


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
