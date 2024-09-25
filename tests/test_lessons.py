#!/usr/bin/python3
"""
Test Lessons class

Modules/Funcs Imported:
unittest: create unittests for python scripts

"""
from models.lessons import Lessons
import unittest
from models.questions import Questions


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

        quiz = new_lesson.Quiz('enzyme_concepts', 'enzymes', 'mcq')

        self.assertEqual(quiz.topic_title, 'enzymes')

        self.assertEqual(quiz.quiz_name, 'enzyme_concepts')

    def test_get_questions(self):
        """Test get_questions() method"""
        new_lesson = Lessons(  # setUp() can be used
            'learn carbohydrates',
            'this is how to easily learn carbohydrates',
            'helping students learn carbohydrates'
        )
        quiz = new_lesson.Quiz('enzyme_concepts', 'enzymes', 'mcq')
        qs = quiz.get_questions('student_12345')

        if not isinstance(qs, list):
            self.fail()

        self.assertEqual(quiz.student_id, 'student_12345')

    def test_result_gen(self):
        """Test result_gen method which calls marker()"""
        new_lesson = Lessons(  # setUp() can be used
            'learn carbohydrates',
            'this is how to easily learn carbohydrates',
            'helping students learn carbohydrates'
        )
        quiz = new_lesson.Quiz('enzyme_concepts', 'enzymes', 'mcq')

        q1 = Questions('Are sugars sweet?', 't/f')

        q2 = Questions('Are carbohydrates sweet', 't/f')

        self.assertEqual(len(quiz.marked_questions), 0)

        # assert both are equal before calling redult_gen()
        self.assertEqual(quiz.questions, quiz.marked_questions)

        gen_questions = [q1, q2]
        result = quiz.result_gen(gen_questions)  # marks question objs
        self.assertEqual(len(quiz.marked_questions), 2)

        # assert both are unequal after calling result_gen()
        self.assertNotEqual(quiz.questions, quiz.marked_questions)

        q1.selected_option = q1.option_selection['T']
        q1.correct_option = q1.option_selection['T']

        q2.selected_option = q2.option_selection['T']
        q2.correct_option = q1.option_selection['F']
        result = quiz.result_gen(gen_questions)  # gen a new result after attempting the questions

        self.assertEqual(result.score, 1)
        self.assertEqual(result.total_questions, 2)
        self.assertEqual(result.percentage_score, '50.0%')
        self.assertEqual(result.status, 'Passed')

        self.assertEqual(len(result.questions_answered_correct), 1)
        self.assertEqual(len(result.questions_answered_correct), 1)

        # more assert here: one answered wrong, one unanswered; both answered correct; both answeted wrong etc
