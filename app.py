import flask
import os
from flask import send_from_directory as send

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='icicle.png')

@app.route('/')
@app.route('/home')
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.secret_key = "aSecret"
    app.debug = True
    app.run()