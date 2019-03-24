from library.flask import Flask, render_template, url_for


app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
