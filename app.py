from flask import render_template, Flask

app: Flask = Flask(__name__)


@app.route('/')
@app.route('/users/<user>')
def hello(user=None):
    return render_template('index.html', name=user)
