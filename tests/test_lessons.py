#!/usr/bin/python3
"""
Test Lessons class

Modules/Funcs Imported:
unittest: create unittests for python scripts

"""
from models.lessons import Lessons
import unittest


class TestLessons(unittest.TestCase):
    """Test the Lessons class and its objects"""

    def test_create_lesson(self):
        """Tests Lessons object creation"""
        try:
             new_lesson = Lessons(
                 'learn carbohydrates',
                 'this is how to easily learn carbohydrates',
                 'helping students learn carbohydrates'
             )
        except (TypeError, ValueError):
            self.fail('TypeError Occured: Invalid arg(s) passed')

        self.assertEqual(
            new_lesson.lesson_title,
             'learn carbohydrates'
        )
        self.assertEqual(
            new_lesson.lesson_content,
            'this is how to easily learn carbohydrates'
        )
        self.assertIsNotNone(new_lesson.lesson_id)


    def test_create_quiz(self):
        """Test creation of a quiz obj"""
        new_lesson = Lessons(
                 'learn carbohydrates',
                 'this is how to easily learn carbohydrates',
                 'helping students learn carbohydrates'
             )
        with self.assertRaises(TypeError):
            quiz = new_lesson.Quiz(1, 't/f')

        quiz = new_lesson.Quiz('enzyme_concepts', 'mcq')

        self.assertEqual(quiz.score, 0)

        self.assertEqual(quiz.quiz_name, 'enzyme_concepts')
