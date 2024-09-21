#!/usr/bin/python3
"""
Test Students class

Modules/Functs Imported:
unittest: create unittests for python scripts
Lessons(class) - create a new lesson
Topics(class) - create a new topic
"""
from models.lessons import Lessons
from models.topics import Topics
import unittest


class TestTopics(unittest.TestCase):
    """Test the Topics class and its objects"""

    def test_create_topic(self):
        """Tests Topics object creation"""
        try:
            monosaccharides = Topics(
                topic_title='monosaccharides',
                course_code=210,
                topic_desc='one molecule sugars',
                topic_lecturer='Mrs Kolawole'
            )
        except TypeError:
            self.fail('TypeError Occured: Invalid arg(s) passed')

        self.assertEqual(monosaccharides.course_code, 210)
        self.assertEqual(monosaccharides.course_title, '')
        self.assertEqual(monosaccharides.course_desc, '')
        self.assertEqual(monosaccharides.topic_desc, 'one molecule sugars')
        self.assertEqual(monosaccharides.topic_lecturer, 'Mrs Kolawole')

    def test_add_lesson(self):
        """Tests add_lesson() in adding a new lesson"""
        obj_topic = Topics(
            'monosaccharides',
            210,
            'one molecule sugars'
        )
        all_lessons_list = obj_topic.lessons  # rem: weird obj behaviour in python
        self.assertEqual(len(all_lessons_list), 0)

        obj_topic.add_lesson(
            'learn carbohydrates',
            'this is how to easily learn carbohydrates',
            'helping students learn carbohydrates'
        )
        self.assertEqual(len(all_lessons_list), len(obj_topic.lessons))
