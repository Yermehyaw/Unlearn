#!/usr/bin/python3
"""
Unlearn console

Imports:
cmd: command line interface in python
sys: access system
Courses, Lessons, Questions, Result, Students, Topics: custom data model clss
storage(obj): instance of storage i.e FileStorage or DB_Storage

"""
import cmd
import sys
from models.courses import Courses
from models.lessons import Lessons
from models.questions import Questions
from models.result import Result
from models.students import Students
from storage import storage
from models.topics import Topics


class UnlearnConsole(cmd.Cmd):
    """
    Unlearn console interface

    """
    if sys.__stdin__.isatty():
        prompt = '(unlearn)'
    elif 'quiz_session':  #quiz session is activated
        prompt = '(Choose your Option)'
