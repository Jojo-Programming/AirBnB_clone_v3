#!/usr/bin/python3
"""flask app"""

from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def  teardown(exception):
    '''close storage connection'''
    storage.close() 

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return jsonify(error="Not found"), 404

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
