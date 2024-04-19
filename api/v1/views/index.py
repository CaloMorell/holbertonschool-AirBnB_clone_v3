#!/usr/bin/python3
"""This module will create a route /status"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """this method creates a route using app_views that returns status"""

    return (jsonify({'status': 'OK'}))

@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def count_classes():
    """This method counts the number of methods"""

    classes = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
    key_names = ["amenities", "cities", "places", "reviews", "states", "users"]
    data = {}
    index = 0
    for type in classes:
        count = storage.count(type)
        data[key_names[index]] = count
        index += 1
    return (jsonify(data))
