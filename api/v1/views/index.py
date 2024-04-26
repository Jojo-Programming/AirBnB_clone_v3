#!/usr/bin/python3xx
'''api status'''

from flask import jsonify
from api.v1.views import app_views


@app.route('/status')
def return_status():
    '''return status'''
    return jsonify(status='OK')
