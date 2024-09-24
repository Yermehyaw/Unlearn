#!/usr/bin/python3
"""
REST api code for rudimentary routes

Modules Imported: app_views, jsonify

app_views(instance): BLueprint instance
jsonify(method): transform objects into JSON
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/', strict_slashes= False)
def welcome():
    """Welcones user to web app"""
    txt = 'Welcome to Unlearn: Redefining the biochemical learning experience'
    return jsonify(txt)

@app_views.route('/login', strict_slashes=False)
def login():
    """Receieve user login for authentication"""
    pass


@app_views.route('/status/<student_id>', strict_slashes=False)
def status(student_id):
    """Return the login status of a student user"""
    # if a not valid student id from storage
    status = {'Logged In': False}
    # else
    # if <condition for login of a studnent>
    status['Logged In'] = True
    return jsonify(status)


@app_views.route('/profile/<student_id>', strict_slashes=False)
def profile(student_id):
    """Return the details of a student"""
    # if student exists in storage
    # get student_id, name, username and created_at details from the
    # student object retrieved from storage
    student_details = {
        'student_id': '',
        'username': '',
        'name': '',
        'created_at': ''
    }
    return jsonify(student_details)
    # else
    return jsonify({'response': 'invalid credential'))
