#!/usr/bin/python3
"""This module will create a route /status"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """this method creates a route using app_views that returns status"""

    return (jsonify({'status': 'OK'}))
