#!/usr/bin/python3
"""
REST api for course topic requests

Modules Imported: app_views, jsonify, Topics

app_views: flask api blueprint
jsonify: convert response to valid json
Topics(cls): Topics class

"""
from views import app_views
from modeks.topics import Topics
from flask import jsonify
from flask import request


@app_views.route('/topics', strict_slashes=False)
def all_topics_count():
    """Returns a dict of all topics"""
    # get total no of topics stored in db
    


@app_views.route(
    '/',
    methods=['GET', 'POST'],
    strict_slashes=False
)
def :
