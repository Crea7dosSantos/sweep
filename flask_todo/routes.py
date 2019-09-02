from flask import render_template, url_for, redirect, jsonify, request
from flask_todo import app, db
from flask_todo.models import Todo, TodoSchema
import json


@app.route('/', methods=('GET',))
def index():
    todos = db.session.query(Todo).all()
    return jsonify({'status': 'ok',
                    'todos': TodoSchema(many=True).dump(todos)})


@app.route('/create', methods=('POST',))
def create():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    data = request.data.decode('utf-8')
    data = json.loads(data)
    title = str(data['title'])
    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/<int:id>delete', methods=('POST',))
def delete(id):
    db.session.query(Todo).filter(Todo.id == id).delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')
