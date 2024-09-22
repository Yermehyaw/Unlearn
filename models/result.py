#!/usr/bin/python3
"""
Result of a quiz session

Modules Imported:
uuid4(mthd): create unique uuid
Quiz(cls): Quiz cls

"""
from uuid import uuid4
from lessons import Quiz


class Result:
    """
    Create a result obj repr the result of a quiz session

    Args:
    quiz_obj(Quiz): obj of quiz session
    student_id(str): id of the student whose result it is(optional)

    Attributes:
    result_id(str): unique id of a result obj
    quiz_id(str): unique id of the quiz which the result obj was generated for
    quiz_name(str): name of the quiz which has this result
    student_id(str): id of the student whose result it is
    score(int): percentage score on the quiz in int
    percentage_score(str): percentage score on the quiz as str
    status(str): passed or failed

    """
    def __init__(self, quiz_obj, user_attempts, student_id=None):
        """Result object initializer"""
        self.result_id = 'result_' + str(uuid4().int)

        if not isinstance(quiz_obj, Quiz):
            raise TypeError('Invalid quiz object')
        else:
            self.quiz_id = quiz_obj.quiz_id
            self.quiz_name = quiz_obj.quiz_name
            self.score = quiz_obj.percentage_score
            self.percentage_score = quiz_obj.percentage_score

        self.percentage_score = 

        if self.percentage_score > 50:
            self.status = 'Passed'
        elif self.percentage_score < 50:
            self.status = 'Failed'

        if course_desc:
            if not isinstance(course_desc, str):
                raise TypeError('Invalid course desc')
            else:
                self.course_desc = course_desc

    @property
    def get_topics_no(self):
        """Returns the no of topics in each course"""
        # retrieve no_topocs from db
        return Courses.no_topics

    @property
    def get_all_topics_list(self):
        """Returns a list of all topics in the course"""
        # retrieve from db
        return Courses.all_topics

    def add_topic(self, new_topic_title, new_cs_code=None):
        """Creates a new topic"""
        new_topic = Topics(new_topic_title, self.course_code)

        Courses.no_topics += 1

        Courses.all_topics.append(new_topic.topic_title)

        return new_topic
