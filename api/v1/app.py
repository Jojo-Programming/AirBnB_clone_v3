#!/usr/bin/python3
"""Flask variable app
"""


from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)



@app.teardown_appcontext
def  teardown_appcontext(exception):
    '''close storage connection'''
    storage.close()

@app.errorhandler(404)
def Not_found(error):
    '''404 error handler'''
    return jsonify('error='Not found'), 404

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host, port, threaded=True)
