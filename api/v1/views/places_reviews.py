#!/usr/bin/python3
"""
Module handles all default RestFul API actions for
Review objects.
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """Return all reviews in a place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = []
    for review in place.reviews:
        reviews.append(review.to_dict())
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """Return a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """Delete a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """Create a review"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.get_json(silent=True):
        abort(400, description="Not a JSON")
    if 'user_id' not in request.get_json(silent=True):
        abort(400, description="Missing user_id")
    if 'text' not in request.get_json(silent=True):
        abort(400, description="Missing text")
    user_id = request.get_json()['user_id']
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    review = Review(**request.get_json(), place_id=place_id)
    review.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """Update a review"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.get_json(silent=True):
        abort(400, description="Not a JSON")
    for key, value in request.get_json().items():
        if key not in ['id', 'user_id', 'place_id', 'created_at',
                       'updated_at']:
            setattr(review, key, value)
    review.save()
    return make_response(jsonify(review.to_dict()), 200)
