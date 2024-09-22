#!/usr/bin/python3
"""
REST api for /quiz requests

Modules Imported: api_views, Courses, jsonify

api_views: flask api blueprint
Courses: Courses class
jsonify: convert response to valid json
make_response: maje http responses
Questions: Questions cls

"""
from views import api_views
from models.courses import Courses
from flask import jsonify
from flask import make_response
from flask import request
from models.questions import Questions


@app_views.route('/quiz/<course_title>', strict_slashes=False)
def all_course_questions(course_title):
    """Returns a dict of all questions in a course"""
    if 1: #  course exists in storage, save as req_course
        topics_in_course = 'req_course.get_all_topics_list'  # a list
        topics_in_course = []  # placeholder, remove
        course_questions = {'course title': 'req_course.course title'}
        for topic in topics_in_course:
            questions_in_topic = topic.questions
            q_list = []
            for question in questions_in_topic:
                question_str = question.question_str
                q_list.append(question_str)
            topic_q = {topic.topic_title: q_list}
            course_questions.update(topic_q)
        return jsonify(course_questions)
    else:
        return jsonify({})

@app_views.route(
    '/quiz/<course_title>/<topic_title>',
    methods=['GET'],
    strict_slashes=False
)
def spec_topic_questions(course_title, topic_title):
    """Returns all questions on a specified topic"""
    if 1:  # course exists, init to req_course
        topics_in_course = 'req_course.get_all_topics_list'  # a list
        topics_in_course = []  # placeholder, remove
        course_questions = {'course title': 'req_course.course title'}
        for topic in topics_in_course:
            if topic.topic_title == topic_title:  # if == to the one user requ
                req_topic = topic  # found the spec requested topic
                questions_in_topic = topic.questions
                q_list = []
                for question in questions_in_topic:
                    question_str = question.question_str
                    q_list.append(question_str)
                topic_q = {topic.topic_title: q_list}
                course_questions.update(topic_q)
        return jsonify(course_questions)

    else:  # course not found in storage
        return jsonify({})
