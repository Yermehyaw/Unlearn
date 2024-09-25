#!/usr/bin/python3
"""
Mini tutorial lessons with quiz for each topic

Modules Imported:
uuid4(method) - generate unique ids
Questions(class) - question bank
Result(cls)
marker(func): marks user attempts of gen questions

"""
from uuid import uuid4
if __name__ == '__main__':
    from questions import Questions
    from result import Result
    from marker import marker
else:
    from .questions import Questions
    from .result import Result
    from .marker import marker


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
        quiz_name(str): name of the quiz
        topic_title(str): name of topic in which quiz is based on
        quiz_type(str): type of quiz questions i.e mcq or t/f
        student_id(str): id of student taking the quiz

        Attributes:
        quiz_id(str): unique id of a quiz
        quiz_name(str): name of quiz
        topic_title(str): name of topic in which quiz is based on
        quiz_type(str): type of quiz e.g MCQ, T/F
        questions(list): list of generated questions for the quiz
        marked_questions(list): answered questions marked
        'corect' or 'wrong' by updating their status attr

        """
        def __init__(
                self,
                quiz_name,
                topic_title,
                quiz_type=None,
                student_id='',
        ):
            """Class initializer"""
            self.quiz_id = 'quiz_' + str(uuid4().int)

            # also check if quiz name already exists in the db
            if not isinstance(quiz_name, str):
                raise TypeError('Invalid quiz name')
            else:
                self.quiz_name = quiz_name
            # should it also be ascertained if the topic exists?
            if not isinstance(quiz_name, str):
                raise TypeError('Invalid quiz name')
            else:
                self.topic_title = topic_title

            if not isinstance(quiz_type, str):
                raise TypeError('Invalid quiz type')
            else:
                self.quiz_type = quiz_type

            self.student_id = student_id
            self.questions = []
            self.marked_questions = self.questions

        def get_questions(self, student_id=''):
            """
            Generates questions from storage for a quiz session

            Args:
            student_id(str): id of student taking the quiz (optional)

            """
            self.student_id = student_id
            # in a loop append question obj from storage to self.questions list
            # call save() (?)
            return self.questions

        def result_gen(self, user_attempts):
            """
            Receives attempts on a quiz from a quiz session and creates a
            Result obj for updating a students progress

            Args:
            user_attempts(list): list of answrered question obj i.e
            with an initialized selected_option attr

            """
            self.marked_questions = marker(user_attempts)
            # call save() (?)
            new_result = Result(self, self.student_id)
            return new_result
