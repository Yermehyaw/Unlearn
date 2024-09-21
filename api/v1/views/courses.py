#!/usr/bin/python3
"""
REST api for courses requests

Modules Imported: api_views, Courses, jsonify

api_views: flask api blueprint
jsonify: convert response to valid json
make_response: maje http responses
Courses: Courses class

"""
from views import api_views
from models.courses import Courses
from flask import jsonify
from flask import make_response
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
        # retrieve from storage and init to req_course
        course_details = {
            'course code': 'req_course.course_code'
            'course title': 'req_course.course_title',
            'description': 'req_course.course_desc',
            'no of topics': 'req_course.get_topics_no',
            'list topics': 'req_course.get_all_topics_list'
        }
        return jsonify(course_details)

    elif request.method == 'POST':
        if 1:  # course already exists:
             return jsonify({'response': 'course already exists'})
        else:  # course not  found in storage
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
        # add to storage using save() via new_course.save()
        resp = jsonify({'response': 'course created successfully'})
        return make_response(resp, 201)
