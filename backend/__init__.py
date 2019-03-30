from flask import Flask, render_template, request
from json import dumps
from database.db import *
from backend.function_for_clean import tokenize_me
from ml.ml_code import ml

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')
database = DB()
problem_table = ProblemsTable(database.get_connection())
users_table = UsersTable(database.get_connection())
cleaning_table = DataToCleaning(database.get_connection())


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Find', methods=['POST'])
def find():
    if request.method == 'POST':
        data = eval(request.data.decode('utf-8'))
        text = data[['searchValue']]
        data = tokenize_me(text)

        answer = {'answers': get_results(ml(data[0])),
                  'deleted': data[1]}
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
            users_table.insert(log, name, pw)
            return dumps('success')

        return dumps('Password Error')


@app.route('/Check', methods=['POST'])
def check_login():
    data = eval(request.data.decode('utf-8'))

    if users_table.get(data['login']):
        return dumps('Login Error')
    return dumps('success')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
