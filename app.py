from flask import Flask, send_file
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, PyNAABO!'

@app.route('/get_image')
def get_image():
    filename = 'logo.webp'
    return send_file(filename)
