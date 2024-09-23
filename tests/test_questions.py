#!/usr/bin/python3
"""
Test Questions class

Modules/Functs Imported:
unittest: create unittests for python scripts
Questions(cls): Make question objs

"""
import unittest
from models.questions import Questions


class TestQuestions(unittest.TestCase):
    """Tests the Courses class and its objects"""

    def test_create_question(self):
        """Tests a new question object for expected behaviour"""
        option_letters = ['A', 'B', 'C', 'D', 'E']  # for testing
        option_arg = ['CH20', 'CHO', 'C2H0', 'CH02', 'NOTA']
        try:
            q1 = Questions(
                'What are sugars?',
                'mcq',
                option_arg
            )
            q2 = Questions(
                'Sugars are always sweet',
                't/f'
            )
        except TypeError:
            self.fail('TypeError Occured: Invalid arg(s) passed')

        with self.assertRaises(TypeError):
            q3 = Questions('Good question text', 'theory', [])
        with self.assertRaises(ValueError):
            q3 = Questions('Good question text', 't/f', ['No options allowed'])
        with self.assertRaises(ValueError):
            q3 = Questions('Good question text', 'mcq', ['A', 'B', 'C', 'D', 'E', 'F'])

        self.assertEqual(q1.tip, '')
        self.assertEqual(q2.tip, '')
        q1.tip = 'The general molecular formula of sugars'
        self.assertNotEqual(q1.tip, '')

        # Assert options passed is saved in the question obj
        q1_options = q1.option_selection.values()
        for key, value in q1_options:
            for letter in option_letters:
                if key == letter:
                    for i in range(5):
                        print(f'{q1_options[key]} == {option_arg[i]}?')
                        self.assertEqual(q1_options[key][0], option_arg[i])
                        break
        q2_options = q2.option_selection
        for key, value in q2_options.items():
                if key == 'True':
                    option_list_val = q1_options[key]
                    for item in option_list_val:
                        if item == 'True':
                            self.assertEqual(, 'True')
                elif key == 'False':
                    option_list_val = q1_options[key]
                    self.assertEqual(option_list_val[0], 'False')

        self.assertEqual(len(q1.selected_option), 0)
        self.assertEqual(len(q1.correct_option), 0)


    def test_show_questions(self):
        """Tests the show_question() mthd in returning proprties of a Questions obj"""
        option_arg = ['CH20', 'CHO', 'C2H0', 'CH02', 'NOTA']
        q1 = Questions(
                'What are sugars?',
                'mcq',
                option_arg
            )
        question_reveal_format = q1.show_question
        print(question_reveal_format)
