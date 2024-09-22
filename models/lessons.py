#!/usr/bin/python3
"""
Mini tutorial lessons with quiz for each topic

Modules Imported:
uuid4(method) - generate unique ids
Questions(class) - question bank

"""
from uuid import uuid4
if __name__ == '__main__':
    from questions import Questions
else:
    from .questions import Questions


class Lessons:
    """
    Create an interactive mini-guide before a quiz attempt

    Args:
    lesson_title(str): title of the lesson
    lesson_content(str): teaching/mentoring content
    lesson_desc(str): lesson details (optional)

    Attributes:
    lesson_id(str): unique lesson id
    lesson_title(str): title of the lesson
    lesson_content(str): teaching/mentoring content
    lesson_desc(str): lesson details

    """
    def __init__(self, lesson_title, lesson_content, lesson_desc=None):
        """Class object initializer"""
        self.lesson_id = 'lesson_' + str(uuid4().int)

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
        quiz_id(str): unique id of a quiz
        quiz_name(str): name of quiz
        quiz_type(str): type of quiz e.g MCQ, T/F
        score(int): total score on a quiz session
        percentage_score(): percentage score on a quiz session
        questions_answered_correct(list): list of Question obj answered correct
        questions_answered_wrong(list): list of Question objs answered wrongly

        """
        def __init__(self, quiz_name, quiz_type=None):
            """Class initializer"""
            self.quiz_id = 'quiz_' + str(uuid4().int)

            # also check if quiz name already exists in the db
            if not isinstance(quiz_name, str):
                raise TypeError('Invalid quiz name')
            else:
                self.quiz_name = quiz_name

            if not isinstance(quiz_type, str):
                raise TypeError('Invalid quiz type')
            else:
                self.quiz_type = quiz_type

            self.score = 0
            self.percentage_score = '0%'
            self.questions_answered_correct = []
            self.questions_answered_wrong = []

        def new_quiz_session(self, student_id=None):
            """
            Prepares a new quiz session for a user

            Args:
            student_id(str): id of student taking the quiz (optional)

            Description:
            1. load questions from db
            2. arrange them in sequential order for 'Next', 'Previous', 'Tip',
            and 'Submit' perusal
            3  Returns a Result object(?) to be used to update a students progress
            """
            # questions = []
            # questions = question_gen()  # func to be imported
            # in a loop append question obj from storage to the list

            # total_questions = len(questions)
            # call marker() func on each resp after 'Next', 'Previous' or 'Submit' is clicked
            # score = 
            # more code

            # session = Result()
            # return session
