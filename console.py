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
        super().__init__()  # retrieve necessary atrr from cmd.Cmd i.e parent cls
        self.found_student = None  # just a placeholder
        self.base_table_list = [
            '', '', '', '',
            '', '', '', '#1 Biochemistry Quiz App'
        ]
        self.unlearn_table = Table(
            title='Unlearn',
            style='black on grey66',
            header_style='white on dark_blue'
        )
        self.unlearn_table.add_column("Unlearn", justify='center')

    def preloop(self):
        """App load up"""
        f = Figlet(font='slant')
        print(f.renderText('Unlearn'))
        print('Redefining the biochemical experience. . ..' + '\n\n')
        storage.reload()  # recreates all previously stored objs in storage
        self.do_home()

    def do_home(self):
        """
        Comprise a dynamic table of chsnging values as interface
        for the unlearn console app

        INFO:
        update_table() isnt used here due to color preferences using the style param 
        """
        self.unlearn_table.add_row('')  # space between values in the table (1)
        self.unlearn_table.add_row("Stop Learning Biochemistry the Wrong Way!", style='text')  # (2)
        self.unlearn_table.add_row('')  # space (3)
        self.unlearn_table.add_row('')  # a row with no value (4)
        self.unlearn_table.add_row('')  # space (5)
        self.unlearn_table.add_row(
            "Sign Up(signup)"
            + (' ' * 5)
            + "Log In(login)"
            + (' ' * 5)
            + "Take a Quick Quiz(start)", style='info'
        )  # (6)
        self.unlearn_table.add_row('')  # space (7)
        self.unlearn_table.add_row('#1 Biochemistry Quiz App')  # (8)
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
            for key, value in objs_in_storage.items():
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
        # Receive user inputs
        arg_fetch = [  # although a name arg isnt required to create a Students() obj, I just decided to stick to the norm and ask for name.
            inquirer.Text('name', message='Name'),
            inquirer.Text('username', message='Username'),
            inquirer.Text('password', message='Password')
        ]
        student_resp = inquirer.prompt(arg_fetch)

        input_username = student_resp['username']
        input_passwd = student_resp['password']
        input_name = student_resp['name']

         if not input_username or not input_passwd:
            print('Username and Password are required')
            return

         if not input_name:
            print('Name is required')
            return

        # Retrieve all available obj from storage
        objs_in_storage = stoarge.load_all()

        # Retrieve only Students() objs from retrieved objs
        student_objs = []
        for key, obj in objs_in_storage.items():
            if (key.split('.'))[0] == 'Students':
                student_objs.append(obj)

        # Search for any existing student with the same username
        for student in student_objs:
            if student.username == student_resp['username']:
                print('User exists already')
                return

        # If it passes the check, create a new user/student
        try:
            new_student = Students(input_username, input_passwd, input_name)
            stoarge.add(new_student)
        except (TypeError, ValueError):
            print('Incorrect signup details entered')
            return

        # save newly created obj to storage
        stoarge.add(new_student)
        storage.save()

    def do_start(self, comd):
        """Creates a new quiz session
        
        Note:
        In future iterations, the user will be able to choose what course
        he/she wishes to be quizzed on. For now, only one course exists i.e BCH210
        """
        if not self.course_created:  # activate this to True when bch210 is created
            create_bch210()
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

    def create_bch210(self):
        """Create bch 210
        A separate py file will be created in future iterations for course creation
        """
        # Create the course obj
        try:
            bch210 = Courses(210, 'Introductory Biochemistry I', 'Introduction to the rudiments of biochemistry for 100l students')
        except (TypeError, ValueError):
            print('Course couldnt be accessed')
            return
        
        # Create a topic in the course
        try:
            bch210_carbohydrates = Topics(
                'carbohydrates',
                bch210.course_code,
                ''
            )

        # Create its questions
        try:
            bch210_questions = Questions() 
        self.course_created = True

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

    def update_table_list(self, index, row_entry):
        """
        Updates the list used to update the rows of 8x1 unlearn_table

        Args:
        index(int): index of the row in unlearn_table to be changed
        row_entry(str): new value of the row

        Description: index 1, 3, 5 and 7 are invalid and are for whitespaces
        to space out values in the table
        """
        invalid = [1, 3, 5, 7]
        if index in invalid:
            raise ValueError('This row cannot be changed')
        # change the list which holds the table
        self.base_table_list[index] = row_entry

    def update_table_rows(self):
        """Use the modified base_table_list to add rows to unlearn_table"""
        self.unlearn_table = Table(  # overwrite previous table with new one
            title='Unlearn',
            style='black on grey66',
            header_style='white on dark_blue'
        )
        self.unlearn_table.add_column("Unlearn", justify='center')

        for list_val in self.base_table_list:
            self.unlearn_table.add_row


if __name__ == '__main__':
    UnlearnConsole().cmdloop()
