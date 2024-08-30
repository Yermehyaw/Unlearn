#!/usr/bin/python3
"""
Courses offered by student

Modules Imported:

"""


class Courses:
    """
    Create a course object representing a course offered by students

    Args:
    course_code(int): unique course code
    course_title(str): name/title of course
    course_desc(str): course details

    Attributes:
    course_code(int): unique course code
    course_title(str): name/title of course
    course_desc(str): course details/description

    """
    no_topics = 0

    def __init__(self, course_code, course_title=None, course_desc=None):
        """Course object initializer"""
        Courses.no_topics += 1

        if not isinstance(course_code, int):
            raise TypeError('Invalid course code')
        else:
            self.course_code = course_code

        self.course_title = course_title
        self.course_desc = course_desc

    @classmethod
    def get_topics_no(cls):
        """Returns the no of topics in each course"""
        return cls.no_topics
