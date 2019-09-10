from flask import jsonify, request
from flask_todo import app, db, bcrypt
from flask_todo.models import Todo, TodoSchema, User
import datetime
from pytz import timezone
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity)


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({"message": "Bad access token"}), 401
        print("not exist current_user")
    print('認証は成功しました')
    print(current_user)
    return jsonify({'status': 'ok',
                    'user_id': current_user})


@app.route('/home', methods=('GET',))
def home():

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


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"msg": "Missing email parameter"}), 400
    if user and bcrypt.check_password_hash(user.password, password):
        print('success signin')
    else:
        return jsonify({"msg": "Missing password parameter"}), 400

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    hashed_pass = bcrypt.generate_password_hash(password)

    user_validate = User.query.filter_by(email=email).first()
    if user_validate:
        return jsonify({"mode": "signup", "status": "error",
                        "message": "This email cannot be used"}), 400

    user = User(username=username, email=email, password=hashed_pass)
    db.session.add(user)
    db.session.commit()
    return jsonify({"mode": "signup", "status": "success",
                    "message": "Completed"}), 200
