#!/usr/bin/python3
"""
Topics under each course taken by student

Modules Imported:
uuid4(method) - generate unique ids
Courses(class) - create a course object

"""
from uuid import uuid4
from .courses import Courses


class Topics(Courses):
    """
    Create a topic under each course offered by a student

    Args:
    course_code(int): unique course code
    topic_title(str): title of the topic
    course_title(str): name/title of course (optional)
    course_desc(str): course details (optional)
    topic_desc(str): topic description (optional)

    Attributes:
    topic_id(int): unique id of a topic
    course_code(int): unique course code
    topic_title(str): title of the topic
    course_title(str): name/title of course
    course_desc(str): course details
    topic_desc(str): topic description

    """
    def __init__(
            self,
            course_code,
            topic_title,
            course_title=None,
            course_desc=None,
            topic_desc=None
    ):
        super().__init__(course_code, course_title, course_desc)

        self.topic_id = uuid4()

        if not isinstance(topic_title, str):
            raise TypeError('Invalid topic title')
        else:
            self.topic_title = topic_title

        if not isinstance(topic_desc, str):
            raise TypeError('Invalid topic desc')
        else:
            self.topic_desc = topic_desc
