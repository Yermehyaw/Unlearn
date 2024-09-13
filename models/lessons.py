#!/usr/bin/python3
"""
Mini tutorial lessons with quiz for each topic

Modules Imported:
uuid4(method) - generate unique ids
Questions(class) - question bank

"""
from uuid import uuid4
from .questions import Questions


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

        self.lesson_desc = lesson_desc
        if lesson_desc:
            if not isinstance(lesson_desc, str):
                raise TypeError('Invalid lesson description')
            else:
                self.lesson_desc = lesson_desc

    class Quiz:
        """
        Interface for answering questions after a lesson. Creates
        a dynamic quiz session

        Args:
        None

        Attributes:
        quiz_id(int): unique id of a quiz
        quiz_name(str): name of quiz
        quiz_type(str): type of quiz e.g MCQ, T/F
        score(int): score on a quiz session

        """
        def __init__(self, quiz_name, quiz_type=None):
            """Class initializer"""
            self.quiz_id = uuid4()

            # also check if quiz nane already exisrs in the db
            if not isinstance(quiz_name, str):
                raise TypeError('Invalid quiz name')
            else:
                self.quiz_name = quiz_name

            if not isinstance(quiz_type, str):
                raise TypeError('Invalid quiz type')
            else:
                self.quiz_type = quiz_type

            self.score = 0

        def new_quiz_session(self):
            """
            Prepares a new quiz session for a user

            Args:
            None

            """
            questions = Questions.get_questions('id_of_a_topic') ###

            # more code

            # session = ##
            # return session
