#!/usr/bin/python3
"""
Courses offered by student

Modules Imported:
uuid4(method) - generate unique ids

"""
from uuid import uuid4


class Courses:
    """
    Create a course object representing a course offered by students

    Args:
    course_code(int): unique course code
    course_title(str): name/title of course
    description(str): course details

    Attributes:
    course_code(int): unique course code
    course_title(str): name/title of course
    description(str): course details/description

    """
    def __init__(self, course_code, course_title=None, description=None):
        """Course object initializer"""
        if isinstance(course_code, int):
            self.course_code = course_code
        else:
            raise TypeError('Invalid course code')

        self.course_title = course_title
        self.description = description
