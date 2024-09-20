#!/usr/bin/python3
"""
Test Students class

Modules/Functs Imported:
unittest: create unittests for python scripts

"""
import unittest
from models.courses import Courses
# from courses import Courses


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

        self.assertEqual(bch_220.course_title, '')

        self.assertEqual(bch_220.course_desc, '')


    def test_add_topic(self):
        """Tests course topic creation"""
        bch_220 = Courses(220)
        with self.assertRaises(TypeError):
            bch_220.add_topic(450)

        no_topics = bch_220.get_topics_no
        all_topics = bch_220.get_all_topics_list

        bch_220.add_topic('ETC')
        self.assertEqual(bch_220.get_topics_no, (no_topics + 1))
        self.assertEqual(bch_220.get_all_topics_list, all_topics)
        # all_topics.append not used: wierd py behaviour with immutable objs
