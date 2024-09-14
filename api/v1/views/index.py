#!/usr/bin/python3
"""
REST api code for rudimentary routes

Modules Imported: app_views, jsonify

app_views(instance): BLueprint instance
jsonify(method): transform objects into JSON
"""
from views import app_views
from flask import jsonify



@app_views.route('/login', strict_slashes=False)
def login():
    """Receieve user login for authentication"""
    pass

@app_views.route('/status/<student_id>', strict_slashes=False)
def status(student_id):
    """Return the login status of a student user"""
    pass
