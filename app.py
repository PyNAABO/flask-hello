import time
from flask import Flask, send_file


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, PyNAABO!'

@app.route('/hello')
def hello_world():
    return 'hello world'+str(time.time())

@app.route('/get_image')
def get_image():
    filename = 'ERROR.gif'
    return send_file(filename, mimetype='image/gif')
