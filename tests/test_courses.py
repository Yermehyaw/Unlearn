#!/usr/bin/python3
"""
Test Students class

Modules/Functs Imported:
pycodestyle: PEP8 coding linter
unittest: create unittests for python scripts

"""
import pycodestyle
import unittest
from models.courses import Courses


class TestCourses(unittest.TestCase):
    """Tests the Courses class and its objects"""

    def test_create_course(self):
        """Tests a Course object for exoected behaviour"""
        try:
            bch_220 = Courses(220)
        except TypeError:
            self.fail('TypeError Occured: Invalid arg(s) passed')

        with self.assertRaises(TypeError):
            bch_220 = Courses('220')

        bch_220 = Courses(220)
        #self.assertIsNone(bch_220.course_title)
        self.assertIsNone(bch_220.course_desc)
