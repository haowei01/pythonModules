import json

from flask import Flask, Response
from flask import request
from werkzeug import secure_filename
from other_func_dir.other_func import test_name


app = Flask(__name__)


@app.route('/')
def hello_world():
    print request.headers
    print request.args
    print request.args.get('key1')
    return 'Hello World!' + test_name()


@app.route('/photos.json', methods=['GET'])
def photos():
    data = json.dumps({'key1': 'value1'})
    resp = Response(
        response=data,
        status=201,
        mimetype='application/json'
    )
    return resp


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    password = request.form['password']
    print uname, password
    return 'OK'


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(filename)
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)
