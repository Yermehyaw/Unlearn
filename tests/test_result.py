#!/usr/bin/python3
"""
Test Result class

Modules/Functs Imported:
unittest: create unittests for python scripts

"""
import unittest
from models.result import Result
from models.students import Students
from models.lessons import Lessons


class TestResult(unittest.TestCase):
    """Tests the Result class and its objects"""

    def test_create_result(self):
        """Tests a Result object for expected behaviour"""
        student = Students('jboy', 'joboy1234', 'Joseph')
        lesson = Lessons('learn enzyme trick', 'de-hydrogen-ase')
        quiz = lesson.Quiz('enzyme_concepts', 'enzymes', 't/f')
        try:
            student_result = Result(quiz, student.student_id)
        except TypeError:
            self.fail('TypeError Occured: Invalid arg(s) passed')

        with self.assertRaises(TypeError):
            student_result = Result('quiz', student.student_id)

        self.assertEqual(student_result.score, 0)

        self.assertEqual(student_result.percentage_score, '0.00%')

        self.assertEqual(student_result.status, 'Failed')

        """
        Activate commented tests when real questions are added to storage inorder
        to gen total_questions used to compute percentage_score
        """
        # with self.assertRaises(ValueError):
            # self.score = 105

        student_result.score = 100
        self.assertEqual(student_result.status, 'Passed')
        # self.assertEqual(student_result.percentage_score, '100.00%')

        student_result.score = 49
        self.assertEqual(student_result.status, 'Failed')
        # self.assertEqual(student_result.percentage_score, '49.00%')

        self.assertEqual(student_result.quiz_id, quiz.quiz_id)

        self.assertEqual(student_result.quiz_name, quiz.quiz_name)
