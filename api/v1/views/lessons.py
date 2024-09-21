#!/usr/bin/python3
"""
REST api for /lessons requests

Modules Imported: api_views, jsonify

api_views: flask api blueprint
jsonify: convert response to valid json
make_respobse: Add http capabilities to api reponses

"""
from views import api_views
from  models.lessons import Lessons
from flask import jsonify
from  flask import make_response
from flask import request


@app_views.route(
    '/lessons/<lesson_title>',
    methods=['GET', 'POST'],
    strict_slashes=False
)
def lesson_details(lesson_title):
    """Returns thr details of a specified lesson title"""
    if request.method == 'GET':
        # if req_lesson is found in storage
        lesson_details = {
            'lesson title': 'req_lesson.lesson_title',
            'lesson content': 're'
            'description': 'req_lesson.lesson_desc',
        }
        return jsonify(lesson_details)
        # else:
            # resp = jsonify({'response': 'lesson not found'})
            # return make_response(resp, 400)

    elif request.method == 'POST':
        if 1:  # lesson already exists in storage
            resp = jsonify({'response': 'lesson already exists'})
            return make_response(resp, 400)
        else:  # dosent already exist in storage
            form_data = request.form
            if form_data:
                for key, value in form_data.items():
                    if key == 'lesson_content' or key == 'teachings':
                        lesson_content = value
                    if key == 'lesson_desc' or key == 'description':
                        lesson_desc = value
            else:
                return jsonify({'response': 'No form data sent'})
            new_lesson = Lessons(lesson_title, lesson_content)
            if lesson_desc:
                new_lesson.lesson_desc = lesson_desc
            resp = jsonify({'response': 'lesson created successfully'})
            return make_response(resp, 201)
