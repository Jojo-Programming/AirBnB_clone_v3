#!/usr/bin/python3
"""
Contains the blueprint for the API
"""
from flask import Blueprint

<<<<<<< HEAD
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
=======

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
>>>>>>> a44c44895cc52bfd37a937490338c524f91ecb7c

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
