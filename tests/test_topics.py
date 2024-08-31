#!/usr/bin/python3
"""
Test Students class

Modules/Functs Imported:
pycodestyle: PEP8 coding linter
unittest: create unittests for python scripts

"""
import pycodestyle
import unittest
from models.topics import Topics


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
