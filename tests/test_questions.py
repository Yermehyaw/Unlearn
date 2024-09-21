#!/usr/bin/python3
"""
Test Questions class

Modules/Functs Imported:
unittest: create unittests for python scripts

"""
import pycodestyle
from models.questions import Questions


class TestQuestions(unittest.TestCase):
    """Tests the Courses class and its objects"""

    def test_create_question(self):
        """Tests a new question object for expected behaviour"""
        try:
            q1 = Questions(
                'What are sugars?',
                'mcq',
                ['CH20', 'CHO', 'C2H0', 'CH02', 'NOTA']
            )
            q2 = Questions(
                'Sugars are always sweet',
                't/f'
            )
        except TypeError:
            self.fail('TypeError Occured: Invalid arg(s) passed')

        with self.assertRaises(TypeError):
            q3 = Questions('Good question text', 'theory', [])

        self.assertEqual(q1.tip, '')
        q1.tip = 'The general molecular formula of sugars'
        self.assertNotEqual(q1.tip, '')
