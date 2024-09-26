#!/usr/bin/python3
"""
Unlearn console

Imports:
cmd: command line interface in python
sys: access system
Courses, Lessons, Questions, Result, Students, Topics: custom data model clss
inquirer(obj): interface for receiving inputs frm user
pyfiglet(obj): print text in ascii art
rich(cls): Format console outputs as rich texts
storage(obj): instance of storage i.e FileStorage or DB_Storage
yaspin(obj): context manager for progress indicator and animations

"""
import cmd
from models.courses import Courses
from rich.console import Console
from  pyfiglet import Figlet
import inquirer
from models.lessons import Lessons
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

    def __init__(self):
        """initializer to ensure some attrs are shared amongst methods"""
            self.found_student = None  # just a placeholder

    def preloop(self):
        """App load up"""
        f = Figlet(font='slant')
        print(f.renderText('Unlearn'))
        print('Redefining the biochemical experience. . ..' + '\n\n')
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
        self.unlearn_table.add_column("Unlearn", justify='center')
        self.unlearn_table.add_row("Stop Learning Biochemistry the Wrong Way!", style='text')
        self.unlearn_table.add_row('')  # space between values in the table
        self.unlearn_table.add_row("Sign Up(signup)" + (' ' * 5) + "Log In(login)" + (' ' * 5) + "Take a Quiz Quiz(start)", style='info')
        self.unlearn_table.add_row('')
        self.unlearn_table.add_row('#1 Biochemistry Quiz App')
        UnlearnConsole.console.print(self.unlearn_table)

    def do_login(self, comd):
        """Logs in a user"""
        # input validation code for later
        arg_fetch = [
            inquirer.Text('username', message='Username'),
            inquirer.Text('password', message='Password')
        ]
        student_resp = inquirer.prompt(arg_fetch)

        if not student_resp['username'] or not student_resp['password']:
            print('Empty username or password not allowed')
            return

        with yaspin(text='Loading...', color='yellow') as spinner:  # loading animation
            # search for all Students obj in storage
            objs_in_storage = storage.load_all()
            student_objs = []
            for key, value in objs_in_storage:
                if (key.split('.'))[0] == 'Students':
                    student_objs.append(values)

            if len(student_objs) == 0:
                print('Incorrect login details entered')
                return

            # Search for the spec student obj with tge same username
            for student in student_objs:
                if student.username == student_resp['username']:
                    self.found_student = student
                    print('Logged In Successfully!')
                    return

            if not self.found_student:
                print('Incorrect login details entered')
                return

        spinner.ok("✔ Done!")

    def do_signup(self, comd):
        """Signs up a new user"""
        # Search for any existig student with the sane username
        for student in student_objs:
            if student.username == student_resp['username']:
                print('User exists already')
                return

    def do_start(self, comd):
        """Creates a new quiz session"""
        self.lesson()
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

    def lesson(self, comd):
        """mini-lesson before a quiz session"""

    def do_continue(self, comd):
        """continue to quiz"""

    def do_quit(self, comd):
        """Exits the app"""
        if self.found_student:
            print(f'Goodbye unlearner {self.found_student.usernane}')
        else:
            print('Goodbye unlearner')
        print()
        exit()

    def do_EOF(self, comd):
        """Handles EIF input"""
        if self.found_student:
            print(f'Goodbye unlearner {self.found_student.usernane}')
        else:
            print('Goodbye unlearner')
        print()
        exit()

if __name__ == '__main__':
    UnlearnConsole().cmdloop()
