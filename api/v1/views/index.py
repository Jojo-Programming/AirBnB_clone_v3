#!/usr/bin/python3
'''api status'''

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def return_status():
    '''return status'''
    return jsonify(status='OK')

@app_views.route('/stats')
def get_stats():
    """gets counts for each object type"""
    stats = {"amenities": storage.count("amenity"),
             "cities": storage.count("city"),
             "places": storage.count("place") ,
             "reviews": storage.count("review") ,
             "states": storage.count("state") ,
             "users": storage.count("user")
    }
    return jsonify(stats)
