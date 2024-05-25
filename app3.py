from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    # Retrieve the user's IP address
    user_ip = request.remote_addr
    return render_template('hello.html', ip=user_ip)


if __name__ == '__main__':
    app.run(debug=True)
