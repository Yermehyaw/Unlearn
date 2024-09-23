#!/usr/bin/python3
"""
Test Result class

Modules/Functs Imported:
unittest: create unittests for python scripts

"""
import unittest
from models.result import Result
from models.students import Students
from models.lessons import Quiz


class TestResult(unittest.TestCase):
    """Tests the Result class and its objects"""

    def test_create_result(self):
        """Tests a Result object for expected behaviour"""
        student = Students('jboy', 'joboy1234', 'Joseph')
        quiz = Quiz('enzyme_concepts', 'enzymes', 't/f')
        try:
            student_result = Result(quiz, student.student_id)
        except TypeError:
            self.fail('TypeError Occured: Invalid arg(s) passed')

        with self.assertRaises(TypeError):
            student_result = Result('quiz', student.student_id)

        self.assertEqual(student.score, 0)

        self.assertEqual(student.status, 'Failed')

        student.score = 100
        self.assertEqual(student.status, 'Passed')

        student.score = 49
        self.assertEqual(student.status, 'Failed')

        self.assertEqual(student.quiz_id, quiz.quiz_id)

        self.assertEqual(student.quiz_name, quiz.quiz_name)

        self.assertEqual(student.percentage_score, '0%')
