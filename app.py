from flask import Flask, send_file
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, PyNAABO!'

@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'logo.webp'
       return send_file(filename)
    else:
       filename = 'ERROR.gif'
       return send_file(filename, mimetype='image/gif')
