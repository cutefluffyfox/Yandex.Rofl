from flask import Flask, render_template, request
from json import dumps
from database.db import *
from backend.function_for_clean import to_normal_form
from ml.ml_code import ml
from sqlite3 import IntegrityError
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')
database = DB()
problem_table = ProblemsTable(database.get_connection())
users_table = UsersTable(database.get_connection())
cleaning_table = DataToCleaning(database.get_connection())
story_table = StoryTable(database.get_connection())


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Find', methods=['POST'])
def find():
    if request.method == 'POST':
        data = eval(request.data.decode('utf-8'))
        text = data['searchValue']
        usr_id = int(data['idUser'])
        date = data['datetime']
        data = to_normal_form(text)

        answer = {'answers': get_results(ml(data[0])),
                  'deleted': data[1]}

        if usr_id != -1:
            story_table.insert(usr_id, text, date)

    else:
        answer = 'not post'

    return dumps(answer)


@app.route('/Record', methods=['POST'])
def record():
    if request.method == 'POST':
        data = eval(request.data.decode('utf-8'))

        if not problem_table.get(data['id']):
            problem_table.insert(data['id'],
                                 data['callback'],
                                 data['reply'],
                                 data['description'])
            cleaning_table.insert(data['id'],
                                  data['description'])
            answer = 'success'

        else:
            answer = 'ID Error'

    else:
        answer = "I don't know what the hell I was thinking"

    return dumps(answer)


@app.route('/Login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = eval(request.data.decode('utf-8'))
        log = data['login']
        password = data['password']
        answer = users_table.check_password(log, password)

        if answer == 'success':
            token = ''.join(choice(
                ascii_uppercase + ascii_lowercase + digits
            ) for _ in range(32))

            users_table.set_token(log, token)

            answer = {'errors': '',
                      'user': users_table.get(log) + (token,)}

        else:
            answer = {'errors': 'error',
                      'user': None}

    else:
        answer = 'This is tha gate to infinity'

    return dumps(answer)


@app.route('/Register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = eval(request.data.decode('utf-8'))
        pw = data['password']
        log = data['login']
        name = data['user_name']

        if users_table.get(data['login']):
            return dumps('Login Error')

        if 6 < len(pw) < 32 and pw.isalnum():
            try:
                users_table.insert(log, name, pw)
                return dumps('success')

            except IntegrityError:
                return dumps('Password Error')

        return dumps('Password Error')


@app.route('/Check', methods=['POST'])
def check_login():
    data = eval(request.data.decode('utf-8'))

    if users_table.get(data['login']):
        return dumps('Login Error')
    return dumps('success')


@app.route('/Story', methods=['POST'])
def story():
    data = eval(request.data.decode('utf-8'))

    return dumps(story_table.get(data['user_id']))


@app.route('/GetAllUsers')
def get_all_users():
    data = eval(request.data.decode('utf-8'))
    answer = {'error': 'Error',
              'users': ''}

    if data['id'] == 3 and data['token'] == users_table.get_token(data['id']):
        answer = {'error': '',
                  'users': users_table.get_all()}

    return dumps(answer)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
