#!/usr/bin/python3
"""
Mini tutorial lessons for each topic

Modules Imported:
uuid4(method) - generate unique ids

"""
from uuid import uuid4


class Lessons:
    """
    Create an interactive mini-guide before a quiz attempt

    Args:
    lesson_title(str): title of the lesson
    lesson_content(str): teaching/mentoring content
    lesson_desc(str): lesson details (optional)

    Attributes:
    lesson_id(int): unique lesson id
    lesson_title(str): title of the lesson
    lesson_content(str): teaching/mentoring content
    lesson_desc(str): lesson details

    """
    def __init__(self, lesson_title, lesson_content, lesson_desc=None):
        """Class object initializer"""
        self.lesson_id = uuid4()

        if not isinstance(lesson_title, str):
            raise TypeError('Invalid lesson title')
        else:
            self.lesson_title = lesson_title

        if not isinstance(lesson_content, str):
            raise TypeError('Invalid lesson content')
        else:
            self.lesson_content = lesson_content

        if lesson_desc:
            if not isinstance(lesson_desc, str):
                raise TypeError('Invalid lesson description')
            else:
                self.lesson_desc = lesson_desc
