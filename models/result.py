#!/usr/bin/python3
"""
Result of a quiz session

Modules Imported:
uuid4(mthd): create unique uuid

"""
from uuid import uuid4


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
    questions_answered_correct(list): list of Question obj answer\
ed correct
    questions_answered_wrong(list): list of Question objs answere\
d wrongly
    questions_unattempted(list): list of unattempted questions

    """
    def __init__(self, quiz_obj, student_id=None):
        """Result object initializer"""
        self.result_id = 'result_' + str(uuid4().int)

        try:
            quiz_obj.quiz_id = quiz_obj.quiz_id
            quiz_obj.quiz_name = quiz_obj.quiz_name
        except AttributeError:
            raise TypeError('Invalid quiz object')
        self.quiz_id = quiz_obj.quiz_id
        self.quiz_name = quiz_obj.quiz_name

        self.score = 0
        self.questions_answered_correct = []
        self.questions_answered_wrong = []
        questions = quiz_obj.marked_questions
        total_questions = len(questions)
        for q in questions:
            if q.status == 'correct':
                self.score += 1
                self.questions_answered_correct.append(q)
            elif q.status == 'wrong':
                self.questions_answered_wrong.append(q)
            elif len(q.status) == 0:
                self.questions_unattempted.append(q)

        if self.score >= 50:
            self.status = 'Passed'
        elif self.score <= 49:
            self.status = 'Failed'

        if total_questions == 0:
            self.percentage_score = '0%'
        else:
            self.percentage_score = str(
                (self.score/total_questions) * 100
            ) + '%'

    @property
    def score(self):
        """Get result score"""
        return self.score

    @score.setter
    def set_score(self, new_score):
        """Update other obj attr as score is updated"""
        questions = quiz_obj.marked_questions
        total_questions = len(questions)
        # Activate when real questioms are added to storage
        # if new_score > total_questions:
            # raise ValueError('Invalid score: score greater total questions')
        # else:
        self.score = new_score
        if total_questions == 0:
            self.percentage_score = '0%'
        else:
            self.percentage_score = str(
                (self.score/total_questions) * 100
            ) + '%'

        if self.score >= 50:
            self.status = 'Passed'
        elif self.score <= 49:
            self.status = 'Failed'
