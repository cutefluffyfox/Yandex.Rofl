from library.flask import Flask, render_template, request
from backend.db import *

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Find', methods=['POST'])
def find():
    if request.method == 'POST':
        data = eval(request.data.decode('utf-8'))
        # return get_result(Here ML is changing the data)
        return get_results(['SD1213575',
                            'SD1213532',
                            'SD1213531',
                            'SD1210912',
                            'SD1210678'])
    return 'not post'


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
