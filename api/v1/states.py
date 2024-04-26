#!/usr/bin/python3

"""A script that:
    - retrieves an object into a valid JSON
    - imports new file
"""

from flask import jsonify, request
from app.models import State
from . import api

@api.route("/states/<int:state_id>", methods=["GET", "DELETE", "PUT"])
def state(state_id):
    state = State.query.get(state_id)
    if not state:
        return jsonify({"error": "Not found"}), 404

    if request.method == "GET":
        return jsonify(state.to_dict())

    if request.method == "DELETE":
        state.delete()
        return jsonify({}), 200

    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400

    for key in data:
        if key in ["id", "created_at", "updated_at"]:
            continue
        setattr(state, key, data[key])

    state.save()
    return jsonify(state.to_dict()), 200


@api.route("/states", methods=["POST"])
def create_state():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400

    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201
