#!/usr/bin/python3
"""
REST api for courses requests

Modules Imported: api_views, Courses, jsonify

api_views: flask api blueprint
jsonify: convert response to valid json
Courses: Courses class
"""
from views import api_views
from models.courses import Courses
from flask import jsonify
from flask import request


@app_views.route('/courses/', strict_slashes=False)
def all_courses():
    """Returns a list of all available courses"""
    # Load all courses from storage
    all_courses = []
    return jsonify(all_courses)


@app_views.route(
    '/courses/<course_code>',
    methods=['GET', 'POST'],
    strict_slashes=False
)
def spec_courses(course_code):
    """Returns the details on a specified course code"""
    if request.method == 'GET':
        # if valid/existing course code
        course_details = {
            'course_code': ''
            'course_title': '',
            'course_desc': '',
            'no_topics': ''
        }
        # 'list topics': []
        return jsonify(course_details)
    if request.method == 'POST':
        # if course code dosent exist
        new_course = Courses(course_code)
        form_data = request.form  # attain any data via a form (not json)
        if form_data:
            for key, value in form_data.items():
                if key == 'course_title' or key == 'course_name':
                    new_course.course_title = value
                if key == 'course_desc' or key == 'description':
                    new_course.course_desc = value
                if key == 'no_topics':
                    new_course.no_topics = value
        # add to storage using save(): new_course.save() (?)
        return jsonify({'response': 'course created successfully'})
        # else:
        return jsonify({'response': 'course creation failed'})
