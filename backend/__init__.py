from flask import Flask, render_template, request
from json import dumps, loads
from json.decoder import JSONDecodeError
from database.db import *
from backend.function_for_clean import tokenize_me
from ml.ml_code import ml
from sqlite3 import IntegrityError
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
from gensim.models.keyedvectors import Word2VecKeyedVectors

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')
database = DB()
problem_table = ProblemsTable(database.get_connection())
users_table = UsersTable(database.get_connection())
cleaning_table = CleaningTable(database.get_connection())
story_table = StoryTable(database.get_connection())
model = Word2VecKeyedVectors.load("../ml/russian_database")
search_total = 0


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Find', methods=['POST'])
def find():
    global search_total

    if request.method == 'POST':
        if search_total > 10:
            answer = {
                'errors': 'server is busy',
                'answers': None,
                'deleted': None
            }
            print(search_total)

        else:
            search_total += 1

            try:
                data = loads(request.data)

            except JSONDecodeError:
                return dumps({
                    'errors': 'Oops',
                    'answers': None,
                    'deleted': None
                })

            indexes = ('searchValue', 'idUser', 'datetime')

            if type(data) is dict and \
                    all([i in data for i in indexes]) and len(data) == len(indexes):
                text = data['searchValue']
                usr_id = int(data['idUser'])
                date = int(data['datetime'])
                data, deleted = tokenize_me(text)
                try:
                    data = get_results(ml(data, model))
                    # for _ in range(len(data)):
                    #    data[_]['description'] = tokenize_me(data[_]['description'], clean=False)

                    answer = {
                        'errors': None,
                        'answers': data,
                        'deleted': deleted
                    }

                    if usr_id != -1:
                        story_table.insert(usr_id, text, date)

                except MemoryError:
                    answer = {
                        'errors': 'server is busy',
                        'answers': None,
                        'deleted': None
                    }

            else:
                answer = {
                    'errors': 'data is not json or wrong json',
                    'answers': None,
                    'deleted': None
                }

            search_total -= 1

    else:
        answer = 'not post'

    return dumps(answer)


@app.route('/Record', methods=['POST'])
def record():
    if request.method == 'POST':
        try:
            data = loads(request.data)

        except JSONDecodeError:
            return dumps('Oops')

        indexes = ('id', 'callback', 'reply', 'description')

        if not (
                type(data) is dict or
                all([i in data for i in indexes]) or
                len(data) == len(indexes)
        ):
            answer = 'data is not json or wrong json'

        elif not problem_table.get(data['id']):

            if len(data['id']) > 2 and data['id'][:2].upper() == 'SD' and data['id'][2:].isdigit():
                problem_table.insert(data['id'],
                                     data['callback'],
                                     data['reply'],
                                     data['description'])
                cleaning_table.insert(data['id'],
                                      data['description'])
                answer = 'success'

            else:
                answer = 'Incorrect id'

        else:
            answer = 'Id already in use'

    else:
        answer = "I don't know what the hell I was thinking"

    return dumps(answer)


@app.route('/Login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            data = loads(request.data)

        except JSONDecodeError:
            return dumps({'errors': 'Oops',
                          'user': None})

        indexes = ('login', 'password')

        if type(data) is dict and \
                all([i in data for i in indexes]) and len(data) == len(indexes):
            log = data['login']
            password = data['password']
            answer = users_table.check_password(log, password)

            if answer == 'success':
                token = ''.join(choice(
                    ascii_uppercase + ascii_lowercase + digits
                ) for _ in range(32))

                users_table.set_token(log, token)

                answer = {'errors': None,
                          'user': users_table.get(log) + (token,)}

            else:
                answer = {'errors': 'error',
                          'user': None}
        else:
            answer = {'errors': 'data is not json or wrong json',
                      'user': None}

    else:
        answer = {'errors': 'is not post',
                  'user': None}

    return dumps(answer)


@app.route('/Register', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            data = loads(request.data)

        except JSONDecodeError:
            return dumps('Oops')

        indexes = ('login', 'user_name', 'password')

        if type(data) is not dict or \
                not all([i in data for i in indexes]) or len(data) != len(indexes):
            answer = 'data is not json or wrong json'

        elif users_table.get(data['login']):
            answer = 'Login Error'

        elif 6 < len(data['password']) < 32 and data['password'].isalnum() \
                and not (data['password'].isdigit() or data['password'].isalpha()):
            try:
                users_table.insert(
                    data['login'],
                    data['user_name'],
                    data['password']
                )
                answer = 'success'

            except IntegrityError:
                answer = 'Login Error'

        else:
            answer = 'Password Error'

        return dumps(answer)


@app.route('/Check', methods=['POST'])
def check_login():
    try:
        data = loads(request.data)

    except JSONDecodeError:
        return dumps('Oops')

    indexes = ('login',)

    if type(data) is not dict or \
            not all([i in data for i in indexes]) or len(data) != len(indexes):
        answer = 'data is not json or wrong json'

    elif users_table.get(data['login']):
        answer = 'Login Error'

    else:
        answer = 'success'

    return dumps(answer)


@app.route('/Story', methods=['POST'])
def story():
    try:
        data = loads(request.data)

    except JSONDecodeError:
        return dumps({'errors': 'Oops',
                      'story': None})

    indexes = ('login', 'name', 'password')

    if type(data) is not dict or \
            not all([i in data for i in indexes]) or len(data) != len(indexes):
        answer = {'errors': 'data is not json or wrong json',
                  'story': None}

    else:
        answer = {'errors': None,
                  'story': story_table.get(data['user_id'])}

    return dumps(answer)


@app.route('/GetAllUsers')
def get_all_users():
    try:
        data = loads(request.data)

    except JSONDecodeError:
        return dumps({'errors': 'Oops',
                      'users': None})

    indexes = ('id', 'token')

    if type(data) is not dict or \
            not all([i in data for i in indexes]) or len(data) != len(indexes):
        answer = {'errors': 'data is not json/dict',
                  'users': None}

    elif data['id'] == 3 and data['token'] == users_table.get_token(data['id']):
        answer = {'error': None,
                  'users': users_table.get_all()}

    else:
        answer = {'errors': 'Error',
                  'users': None}

    return dumps(answer)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
