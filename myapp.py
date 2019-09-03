import pymysql
from flask import Flask, redirect, render_template, request, url_for
import setting
from form import CreateTodoForm

app = Flask(__name__)

app.config['SECRET_KEY'] = setting.SECRET_KEY

conn = pymysql.connect(
    host='localhost',
    user=setting.USER_NAME,
    password=setting.PASSWORD, db=setting.DB_NAME,
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor
)
db = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
@app.route('/create', methods=['GET', 'POST'])
def index():
    form = CreateTodoForm()
    if form.validate_on_submit():
        input_form_data = request.form['todo_name']
        db.execute('INSERT INTO todos(name) VALUES (%s)', (input_form_data,))
        return redirect(url_for('index'))

    db.execute('SELECT * from todos')
    todos = db.fetchall()
    return render_template('index.html', form=form, todos=todos)


@app.route('/<int:id>delete', methods=('POST',))
def delete(id):
    db.execute('DELETE FROM todos WHERE id = %s', (id,))
    return redirect(url_for('index'))


app.run(debug=True)
