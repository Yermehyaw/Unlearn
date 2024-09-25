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
    _score(int): score on the quiz
    _percentage_score(int): percentage score on the quiz
    total_questions(int): total no of questions attempted/marked by marker()
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

        self._score = 0
        self.questions_answered_correct = []
        self.questions_answered_wrong = []

        questions = quiz_obj.marked_questions
        self.total_questions = len(questions)

        for q in questions:
            if q.status == 'correct':
                self._score += 1
                self.questions_answered_correct.append(q)
            elif q.status == 'wrong':
                self.questions_answered_wrong.append(q)
            elif len(q.status) == 0:
                self.questions_unattempted.append(q)


        if self.total_questions == 0:
            self._percentage_score = 0.00
        else:
            float_score = float(self._score) / self.total_questions * 100
            self._percentage_score = round(float_score, 2)

        if self._percentage_score >= 50:
            self.status = 'Passed'
        elif self._percentage_score <= 49:
            self.status = 'Failed'

    @property
    def score(self):
        """Get result score"""
        return self._score

    @score.setter
    def score(self, new_score):
        """Update other obj attr as score is updated"""
        # Activate when real questioms are added to storage
        # if new_score > self.total_questions:
            # raise ValueError('Invalid score: score greater total questions')
        # else:
        self._score = new_score
        if self.total_questions == 0:
            self._percentage_score = 0.00
        else:
            float_score = float(self._score) / self.total_questions * 100
            self._percentage_score = round(float_score, 2)

        if self._percentage_score >= 50:
            self.status = 'Passed'
        elif self._percentage_score <= 49:
            self.status = 'Failed'

    @property
    def percentage_score(self):
        """Returns percentage_score as a string with the % sign"""
        str_p_score = str(self._percentage_score) + '%'
        return str_p_score
