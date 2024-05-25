from flask import Flask, url_for

app: Flask = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
