import flask
import requests

app = flask.Flask(__name__, static_url_path=None)

@app.route('/')
def root():
    return 'Hello World'
