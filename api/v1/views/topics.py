#!/usr/bin/python3
"""
REST api for course topic requests

Modules Imported: app_views, SQLALchemy, jsonify, Topics

app_views: flask api blueprint
jsonify: convert response to valid json
Topics(cls): Topics class
SQLAlchemy: ORM for flask apps

"""
from views import app_views
from models.topics import Topics
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLALchemy


@app_views.route('/topics', strict_slashes=False)
def all_topics_count():
    """Returns a dict of all topics"""
    # get total no of topics stored in storage
    total = 0  # change when retrieved from storage
    total = {'Total topics': total}
    return jsonify(total)
    
@app_views.route(
    '/topics/<topic_title>',
    methods=['GET', 'POST'],
    strict_slashes=False
)
def all_topics_list:
    """Returns a list of all topics of a course title
    or creates a new course"""
    if request.method == 'GET':
        # check if its a valid course code from storage

