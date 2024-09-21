#!/usr/bin/python3
"""
REST api for course topic requests

Modules Imported: app_views, SQLALchemy, jsonify, Topics

app_views: flask api blueprint
jsonify: convert response to valid json
make_response: add http features to api responses
Topics(cls): Topics class
SQLAlchemy: ORM for flask apps

"""
from views import app_views
from models.topics import Topics
from flask import jsonify
from flask import make_response
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
    '/topics/<course_title>',
    methods=['GET', 'POST'],
    strict_slashes=False
)
def all_topics_list(course_title):
    """Returns a list of all topics of a course title
    or creates a new course"""
    if request.method == 'GET':
        # check if its a valid course code from storage
        # retrieve coourse obj from storage as req_course
        course_topics = {
            'course code': 'req_course.course_code',
            'course title': 'req_course.course_title'
            'topics': 'req_course.get_all_topics_list'
        }
        return jsonify(course_topics)
    elif request.method == 'POST':
        if 1:  # course exists
            form_data = request.form_data
            if form_data:
                for key, value in form_data.items():
                    if key == 'topic title' or key == 'topic name':
                        # filter input during security implement
                        new_topic_title = value
            else:
                return jsonify({'response': 'No form data sent'})
            new_topic = 'req_course.add_topic(new_topic_title)'
            resp = jsonify({'response': 'topic created successfully'})
            return make_response(resp, 201)
        else:  # course dosent exist, course must exist to have a topic
            return make_response(jsonify({'response': 'course not found'}), 400)
