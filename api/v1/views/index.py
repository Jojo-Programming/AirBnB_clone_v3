#!/usr/bin/python3
"""api status"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """display api the status"""
    return jsonify(status="OK")

@app_views.route('/stats', strict_slashes=False)
def stats():
    """count number of each objects by type"""
    classes = {'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review}
    for key in classes:
        classes[key] = storage.count(classes[key])
    return jsonify(classes)
