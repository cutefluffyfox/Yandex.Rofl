from library.flask import Flask, render_template, request
from json import dumps

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/Find', methods=['POST'])
def find():
    if request.method == 'POST':
        data = eval(request.data.decode('utf-8'))

        # Here ML is changing the data

        return dumps(data)
    return 'not post'


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
