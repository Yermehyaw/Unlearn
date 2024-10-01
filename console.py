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
        self.student_found = None  # just a placeholder
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
                    self.student_found = student
                    print('Logged In Successfully!')
                    return

            if not self.student_found:
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
        objs_in_storage = storage.load_all()

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
           self.student_new = Students(input_username, input_passwd, input_name)
            storage.add(student_new)
        except (TypeError, ValueError):
            print('Incorrect signup details entered')
            return

        # save newly created obj to storage
        storage.add(student_new)
        storage.save()

    def do_start(self, comd):
        """Creates a new quiz session

        Note:
        In future iterations, the user will be able to choose what course he/she
        wishes to be quizzed on. For now, only one course exists i.e BCH210
        """
        if not self.course_created:  # activate this to True when bch210 is created
            self.create_bch210()
        print('Beginning lesson on carbohydrates')
        print('')
        self.lesson('carbohydrates')  # this is where the appr lessonon the topic which the student has selected will be called
        try:
            self.quiz_session = self.intro_carbohydrates.Quiz()  # only intro to carb lesson is available
        except (TypeError, ValueError):
            print('Quiz could not be accessed. Please try again later')
            return

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
        storage.save(bch210)  # save to storage

        # Create a topic in the course
        try:
            bch210_carbohydrates = Topics(
                'carbohydrates',
                bch210.course_code,
                ''
            )
        except (TypeError, ValueError):
            print('Topic couldnt be accessed')
            return
        storage.save(bch210_carbohydrates)

        # Create its questions
        try:
            bch210_q1 = Questions(
                '___ are the precursors of virtually all other biomolecules',
                'mcq',
                options=['proteins', 'enzymes', 'hydrocarbons', 'carbohydrates', 'lipids'],
                tip='It is the "skeleton" of lipids'
            )
            bch210_q1.correct_option.append('carbohydrates')

            bch210_q2 = Questions(
                'The characteristic chemical feature of carbohydrates includes all of the following except?',
                'mcq',
                options=[
                    'The existence of at least one asymmetruc centers',
                    'The ability to exist in ring or linear structure',
                    'The capacity to form polymeric form by glycosidic bond',
                    'The inability to form multiple hydrogen bonds with water',
                    'The ability to form multiple hydrogen boonds with water'
                ],
                tip='For a substance to form hydrigen bonds, it must exhibit some measure of polarity or contain an OH group'
            )
            bch210_q2.correct_option.append('The inability to form multiple hydrogen boonds with water')

            bch210_q3 = Questions(
                'A generic name is important in describing monosaccharides because ____',
                'mcq',
                [
                    'It tells us both the important functional groups and the total number of asymmetric centers',
                    'It tells us both the important functional groups and the total number of hydroxyl atoms',
                    'It tells us both the total no of carbon atoms and the important functional groups',
                    'All of the above',
                    'None of the above'
                ],
                'The major differntiator between two or more generic names are based on differences on a shared characteristic'
            )
            bch210_q3.correct_option.append('It tells us both the total no of carbon atoms and the important functional groups')

            bch210_q4 = Questions(
                'Ketopeptones include',
                'mcq',
                [
                    'Psicose',
                    'Fructose',
                    'Sorbose',
                    'Ribulose',
                    'Xylulose'
                ],
                'Keto sugars have more than an -ose appeneded to their names'
            )
            bch210_q4.correct_option.append('Ribulose')

            bch210_q5 = Questions(
                'Which of the following statement about mutarotation is NOT correct?',
                'mcq',
                [
                    'Spontaneous change in the optical rotation of sugars',
                    'Interconversion of the alpha and beta forms of the monosaccharide',
                    'alpha D-glucose has a specific optical rotation of 112°',
                    'beta D-glucose has a specific optical rotation of 18.7°',
                    'None of the above'
                ],
                'Mutarotation pertains to optical property alone'
            )
            bch210_q5.correct_option.append('Interconversion of the alpha and beta forms of the monosaccharide')

            bch210_q6 = Questions(
                'Glucose reacts with alkaline CuSO4 to form red cuprois oxide ppt and ____',
                'mcq',
                [
                    'Gluconic acid',
                    'Glucoronic acid',
                    'Glucaric acid',
                    'L-Iduronic acid'
                ],
                'The stronger the O.A reacting with glucose, the more the name of the resulting acid departs from the original "glucose"'
            )
            bch210_q6.correct_option.append('Gluconic acid')

            bch210_q7 = Questions(
                'Monosaccharides can be oxidized enzymatically at carbon 6 yielding ____',
                'mcq',
                [
                    'Uronic acid e.g D-glucoronic acid',
                    'Aldonic acid e.g gluconic acid',
                    'Aldaric acid e.g glucaric acid',
                    'All of the above',
                    'None of the above'
                ],
                'All ald -acids are formed by oxidizing the carbon with tge functional group'
            )
            bch210_q7.correct_option.append('Uronic acid e.g D-glucoronic acid')

            bch210_q8 = Questions(
                'Galactose is a C2 epimer of glucose',
                't/f',
                tip='Mannose comes before Galactose'
            )
            bch210_q8.correct_option.append('False')

            bch210_q9 = Questions(
                'The important constituent of the vitreous humor of the eye and synovial fluid is hyaluronic acid',
                't/f',
                tip='hylarunoic is derived from the greek work hyla which means "glass" or "glass-like"'
            )
            bch210_q9.correct_option.append('True')

            bch210_q10 = Questions(
                'Cellobiose is a non reducing sugar',
                't/f',
                tip='Non reducing sugars are commonly NOT derivates of highrt polysaccharides and are mostly disaccharides'
            )
            bch210_q10.correct_option.append('False')

        except (TypeError, ValueError):
            print('Course couldnt be accessed')
            return
        # save all questions to storage
        storage.save(bch210_q1)
        storage.save(bch210_q2)
        storage.save(bch210_q3)
        storage.save(bch210_q4)
        storage.save(bch210_q5)
        storage.save(bch210_q6)
        storage.save(bch210_q7)
        storage.save(bch210_q8)
        storage.save(bch210_q9)
        storage.save(bch210_q10)

        self.course_created = True

    def lesson(self, topic_name):
        """mini-lesson before a quiz session"""
        if topic_name == 'carbohydrates':
            try:
                self.intro_carbohydrates = Lessons(
                    'Introduction to carbohydrates',
                    'Carbohydrates are vital organic compounds classified into three main types: monosaccharides, disaccharides, and polysaccharides. Monosaccharides, such as glucose and fructose, are simple sugars that serve as energy sources. Disaccharides, like sucrose and lactose, consist of two monosaccharides linked together. Polysaccharides, including starch, glycogen, and cellulose, are complex carbohydrates made of long chains of monosaccharides. They play crucial roles in energy storage, structural support, and cellular functions in living organisms.',
                    'Informs the student on only the types of carbohydrates without listing key characteristics of each nor their uses'
                )
            except (TypeError, ValueError):
                print('Lesson to be quizzed on cannot be accessed')
                return

    def do_continue(self, comd):
        """continue to quiz"""

    def do_quit(self, comd):
        """Exits the app"""
        if self.student_found:
            print(f'Goodbye unlearner {self.student_found.usernane}')
        else:
            print('Goodbye unlearner')
        print()
        exit()

    def do_EOF(self, comd):
        """Handles EOF input"""
        if self.student_found:
            print(f'Goodbye unlearner {self.student_found.usernane}')
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
