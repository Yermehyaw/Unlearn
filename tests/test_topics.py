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
                210,
                'monosaccharides',
                'carbohydrates',
                'sugars in biochemistry',
                'one molecule sugars'
            )
        except TypeError:
            self.fail('TypeError Occured: Invalid arg(s) passed')

        self.assertEqual(monosaccharides.course_code, 210)
        self.assertEqual(monosaccharides.course_title, 'carbohydrates')
        self.assertNotEqual(monosaccharides.course_desc, '')
        self.assertIsNotNone(monosaccharides.topic_desc)

    def test_add_lesson(self):
        """Tests add_lesson() in adding a new lesson"""
        obj_topic = Topics(
            210,
            'monosaccharides',
            'carbohydrates',
            'sugars in biochemistry',
            'one molecule sugars'
        )
        obj_topic.add_lesson(  # add a new lesson
            'learn carbohydrates',
            'this is how to eaily learn carbohydrates',
            'helping students learn carbohydrates'
        )
        obj_lesson = Lessons(  # create a duplicate of the object
            'learn carbohydrates',
            'this is how to eaily learn carbohydrates',
            'helping students learn carbohydrates'
        )

        for lesson_dict in obj_topic.lessons:
            for key, value in lesson_dict():
                if key != 'lesson_id':
                    self.assertEqual(value, obj_lesson.key)
                    self.assertNotEqual(
                        obj_topic.lessons['lesson_id'],
                        obj_lesson.lesson_id
                    )
