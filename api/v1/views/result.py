#!/usr/bin/python3
"""
REST api for /result requests

Modules Imported: api_views, Courses, jsonify

api_views: flask api blueprint
jsonify: convert response to valid json

"""
from views import api_views
from flask import jsonify


@app_views.route(
    '/result/<quiz_id>/<student_id>',
    methods=['GET'],
    strict_slashes=False
)
def spec_quiz_result(quiz_id, student_id):
    """Returns the latest result on a quiz by a student"""
    if 1:  # quiz exists, init to req_quiz
        if 1: # student_id exists, student_id and req_quiz.student_id are equal and len(req_quiz.student_id) != 0
            """
            1. acquire student name from storage using student id (optional). init to student_name
            2. using quiz_id and student_id find the latest req_result
            which will be the only quiz result since new quiz result overwrites
            previous ones thats why the gen resukt must be immediautely addednto a students progress
            """
            result_details = {
                'student id': student_id,
                'quiz name': 'req_result.quiz_name',
                'total score': 'req_result.score',
                'percentage score': 'req_result.percentage_score',
                'status': 'req_result.status'
            }
            # 'student name': 'student_name',
            return jsonify(result_details)

        else:  # student_id not found or student_id and req_quiz.student_id are not equal or len(req_quiz.student_id) == 0
            return jsonify({})

    else:  # quiz not found in storage
        return jsonify({})
