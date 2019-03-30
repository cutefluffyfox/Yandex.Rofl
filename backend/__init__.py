from flask import Flask, render_template, request
from json import dumps
from database.db import *
from backend.function_for_clean import tokenize_me
from ml.ml_code import ml

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Find', methods=['POST'])
def find():
    if request.method == 'POST':
        text = eval(request.data.decode('utf-8'))['searchValue']
        # print(1)
        text = tokenize_me(text)
        # print(text)
        res = ml(text)
        # print(res)
        return get_results(res)
        # return dumps(get_results(['SD1213575',
        #                           'SD1213532',
        #                              'SD1213531',
        #                           'SD1210912',
        #                           'SD1210678']))
    return 'not post'


@app.route('/Record', methods=['POST'])
def record():
    if request.method == 'POST':
        data = eval(request.data.decode('utf-8'))
        database = DB()
        problem_table = ProblemsTable(database.get_connection())

        if problem_table.get(data['id']):
            problem_table.insert(data['id'],
                                 data['callbacks'],
                                 data['reply'],
                                 data['description'])
            answer = 'success'

        else:
            answer = 'ID Error'

        return dumps(answer)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
