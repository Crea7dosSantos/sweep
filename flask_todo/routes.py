from flask import url_for, redirect, jsonify, request
from flask_todo import app, db
from flask_todo.models import Todo, TodoSchema
import json
import datetime
from pytz import timezone


@app.route('/index', methods=('GET',))
def index():
    todos = db.session.query(Todo).all()
    for todo in todos:
        dt_naive_to_utc_replace = todo.date_posted.replace(
            tzinfo=datetime.timezone.utc)
        todo.date_posted = dt_naive_to_utc_replace.astimezone(
            timezone('Asia/Tokyo'))

    return jsonify({'status': 'ok',
                    'todos': TodoSchema(many=True).dump(todos)})


@app.route('/create', methods=('POST',))
def create():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    title = request.json.get('title', None)
    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()
    return 'OK'


@app.route('/delete', methods=('POST',))
def delete():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    id = request.json.get('delete_id', None)
    db.session.query(Todo).filter(Todo.id == id).delete()
    db.session.commit()
    return 'OK'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'OK'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return 'OK'
