import pymysql
from flask import Flask, redirect, render_template, request, url_for

# flaskアプリケーションの作成
app = Flask(__name__)

conn = pymysql.connect(host='localhost', user='flask_user',
                       password='yusaku0720', db='flask_db', autocommit=True,
                       cursorclass=pymysql.cursors.DictCursor)
db = conn.cursor()


@app.route('/')
def index():
    db.execute('SELECT * from todos')
    todos = db.fetchall()
    return render_template('index.html', todos=todos)


@app.route('/create', methods=('POST',))
def create():
    name = request.form['name']
    db.execute('INSERT INTO todos(name) VALUES (%s)', (name,))
    return redirect(url_for('index'))


@app.route('/<int:id>delete', methods=('POST',))
def delete(id):
    db.execute('DELETE FROM todos WHERE id = %s', (id,))
    return redirect(url_for('index'))


app.run(debug=True)
