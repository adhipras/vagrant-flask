#!/usr/bin/env python

from flask import Flask, jsonify, request
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)


@app.route('/')
def view_headers():
    d = dict(
        headers=dict(request.headers.items()),
        origin=request.environ['REMOTE_ADDR']
    )
    return jsonify(d)


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
