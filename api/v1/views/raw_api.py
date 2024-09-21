#!/usr/bin/python3
"""
REST api for . . . requests

Modules Imported: api_views, jsonify

api_views: flask api blueprint
jsonify: convert response to valid json
make_respobse: Add http capabilities to api reponses

"""
from views import api_views

from flask import jsonify
from  flask import make_response
from flask import request


@app_views.route('/', strict_slashes=False)
def :


@app_views.route(
    '/',
    methods=['GET', 'POST'],
    strict_slashes=False
)
def :
