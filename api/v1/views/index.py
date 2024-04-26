#!/usr/bin/python3

"""A Script that:
    -creates a route tonthe project
    - returns JASON
"""

from flask import jsonify

# Import your blueprint (assuming it's named bp)
from . import bp

@bp.route("/status")
def status():
  """
  Return a JSON response with the status "OK".
  """
  return jsonify({"status": "OK"})
