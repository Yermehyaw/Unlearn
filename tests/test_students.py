#!/usr/bin/python3
"""
Test Students class

Modules/Functs Imported:
pycodestyle: PEP8 coding linter
unittest: create unittests for python scripts

"""
import pycodestyle
import unittest
from Unlearn.models.students import Students


class TestStudents(unittest.TestCase):
    """Test the Students class and its objects"""

    def test_pep8_validation(self):
        """Tests for pep8 compliance"""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['../models/students.py'])
        self.assertEqual(result.total_errors, 1, "Pycodestyle Errors Found")

    def test_create_student(self):
        """Tests a Students object for expected behaviour"""
        try:
            student = Students('johnny', 'johny1234', name='John')
        except TypeError:
            self.fail('TypeError Occured: Invalid arg(s) passed')

        self.assertEqual(student.name, 'John')
        self.assertEqual(student.username, 'johnny')
        self.assertNotEqual(student.p_hash, 'johnny1234')
