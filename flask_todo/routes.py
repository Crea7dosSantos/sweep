from flask import jsonify, request
from flask_todo import app, db, bcrypt
from flask_todo.models import Todo, TodoSchema, User, UserSchema
import datetime
from pytz import timezone
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required,
    jwt_refresh_token_required, get_jwt_identity, )


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({"message": "Bad access token"}), 401
    user_datas = db.session.query(User.username, User.email, User.id).\
        filter(User.id == current_user)
    return jsonify({'status': 'ok',
                    'user_datas': UserSchema(many=True).dump(user_datas)}), 200


@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({"message": "Bad access token"}), 401
    new_token = create_access_token(identity=current_user, fresh=False)
    ret = {'access_token': new_token}
    return jsonify(ret), 200


@app.route('/home', methods=('GET',))
@jwt_required
def home():
    current_user = get_jwt_identity()
    print(current_user)
    todos = db.session.query(Todo).filter(Todo.user_id == current_user).all()
    for todo in todos:
        dt_naive_to_utc_replace = todo.date_posted.replace(
            tzinfo=datetime.timezone.utc)
        todo.date_posted = dt_naive_to_utc_replace.astimezone(
            timezone('Asia/Tokyo'))

    return jsonify({'status': 'ok',
                    'todos': TodoSchema(many=True).dump(todos)}), 200


@app.route('/create', methods=('POST',))
@jwt_required
def create():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    current_user = get_jwt_identity()
    title = request.json.get('title', None)
    todo = Todo(title=title, user_id=current_user)
    db.session.add(todo)
    db.session.commit()
    return jsonify({"message": "Success create Todo"}), 200


@app.route('/delete', methods=('POST',))
@jwt_required
def delete():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    id = request.json.get('delete_id', None)
    db.session.query(Todo).filter(Todo.id == id).delete()
    db.session.commit()
    return jsonify({"message": "Success delete Todo"}), 200


@app.route('/signin', methods=['POST'])
def signin():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if not user:
        # abort(400, {"msg": "Missing email parameter"})
        return jsonify({"msg": "Missing email parameter"}), 400
    if user and bcrypt.check_password_hash(user.password, password):
        print('success signin')
    else:
        return jsonify({"msg": "Missing password parameter"}), 400

    ret = {
        'access_token': create_access_token(identity=user.id, fresh=True),
        'refresh_token': create_refresh_token(identity=user.id)
    }
    return jsonify(ret), 200


@app.route('/signup', methods=['POST'])
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


@app.route('/signout', methods=['POST'])
def signout():
    return jsonify({"mode": "signout", "status": "success",
                    "message": "Completed"}), 200


@app.route('/profile', methods=['GET'])
@jwt_required
def profile():
    current_user = get_jwt_identity()
    print(current_user)
    user = db.session.query(User).filter(User.id == current_user).all()
    print(user)

    return jsonify({'status': 'ok',
                    'user': UserSchema(many=True).dump(user)}), 200
