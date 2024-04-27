#!/usr/bin/python3
"""Flask variable app
"""


from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def  teardown_appcontext(self):
    '''close storage connection'''
    storage.close()

@app.errorhandler(404)
def Not_found(error):
    '''404 error handler'''
    return jsonify('error='Not found), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

