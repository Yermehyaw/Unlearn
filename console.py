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
from rich.console import Console
import inquirer
from models.lessons import Lessons
import pyfiglet
from models.questions import Questions
from models.result import Result
from models.students import Students
from rich.table import Table
from rich.theme import Theme
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

    unlearn_theme = Theme(
        {
            "info": "bold cyan", "text": "bright_blue",
            "bg": "thistle1",  "warning": "magenta",
            "danger": "bold red"
        }
    )
    console = Console(theme=unlearn_theme)

    def preloop(self):
        """App load up"""
        storage.reload()
        self.do_home()

    def do_home(self):
        """
        Comprise a dynamic table of chsnging values as interface
        for the unlearn console app
        """
        self.unlearn_table = Table(
            title='Unlearn',
            style='black on grey66',
            header_style='white on dark_blue'
        )
        self.unlearn_table.add_column("Unlearn")
        self.unlearn_table.add_row("Stop Learning Biochemistry the Wrong Way!", style='text')
        self.unlearn_table.add_row("Sign Up(signup)" + (' ' * 5) + "Log In(login)" + (' ' * 5) + "Take a Quiz Quiz(start)", style='bg')
        self unlearn_table.add_row('#1 Biochemistry Quiz App')
        UnlearnConsole.console.print(self.unlearn_table)

    def do_login(self, comd):
        """Logs in a user"""

    def do_proceed(self, comd):
        """Proceeds to finish login/user authentication"""

    def do_signup(self, comd):
        """Signs up a new user"""

    def do_finish(self, comd):
        """Finish user sign uo/ create new student"""

    def do_start(self, comd):
        """Creates a new quiz session"""
        self.do_lesson()
        print('')

    def do_A(self):
        """Option A is chosen"""

    def do_B(self):
        """Option B is chosen"""

    def do_C(self):
        """Option C is chosen"""

    def do_D(self):
        """Option D is chosen"""

    def do_E(self):
        """Option E is chosen"""

    def do_T(self):
        """True is chosen"""

    def do_F(self):
        """False is chosen"""

    def do_p(self, comd):  # is athe do_prefix necessary?
        """Navigate to previous question"""

    def do_n(self, comd):
        """Navigate to the next question"""

    def do_i(self, cond):
        """Give user a tip on the question"""

    def do_submit(self, comd):
        """Submit attempted questions"""

    def do_lesson(self, comd):
        """mini-lesson before a quiz session"""

    def do_continue(self, comd):
        """continue to quiz"""

    def do_quit(self, comd):
        """Exits the app"""
        print()
        exit()

    def do_EOF(self, comd):
        """Handles EIF input"""
        print()
        exit()

if __name__ == '__main__':
    UnlearnConsole().cmdloop()
