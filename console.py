#!/usr/bin/python3
"""
Unlearn console

Imports:
cmd: command line interface in python
sys: access system
Courses, Lessons, Questions, Result, Students, Topics: custom data model clss
inquirer(obj): interface fore receiving inputs frm user
pyfiglet(obj): print text in ascii art
rich(cls): Format console outputs as rich texts
storage(obj): instance of storage i.e FileStorage or DB_Storage
yaspin(obj): context manager for progress indicator and animations

"""
import cmd
from models.courses import Courses
import inquirer
from models.lessons import Lessons
import pyfiglet
from models.questions import Questions
from models.result import Result
import rich
from models.students import Students
from storage import storage
import sys
from models.topics import Topics
from yaspin import yaspin


class UnlearnConsole(cmd.Cmd):
    """
    Unlearn console interface

    """
    if sys.__stdin__.isatty():
        prompt = '(unlearn) '

    def unlearn_home(self):
        """
        Comprise a dynamic table of chsnging values as interface
        for the unlearn console app
        """

    def do_L(self):
        """Logs in a user"""

    def do_U(self):
        """Signs up a new user"""

    def do_take_quiz(self):
        """Creates a new quiz session"""
        do_lesson()

        def do_previous(self):  # is athe do_prefix necessary?
            """Navigate to previous question"""

        def do_next(self):
            """Navigate to the next question"""

        def do_tip(self):
            """Give user a tip on the question"""

        def do_submit(self):
            """Submit attempted questions"""

    def do_lesson(self):
        """mini-lesson before a quiz session"""

        def do_back(self):
            """Return back to home"""

        def do_continue(self):
            """continue to quiz"""

    def do_quit(self, command):
        """Exits the app"""
        print()
        exit()

    def do_EOF(self, command):
        """Handles EIF input"""
        print()
        exit()

if __name__ == '__main__':
    UnlearnConsole().cmdloop()
