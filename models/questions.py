#!/usr/bin/python3
"""
Question bank for the unlearn app

Modules Imported:
uuid4(method) - generate unique ids

"""
from uuid import uuid4


class Questions:
    """
    Questions class

    Args:
    question_str(str): question to be asked
    option_type(str): type of option the question has i.e either mcq or t/f
    options(list): list of options
    tip(str): a tip to aid user

    Attributes:
    question_id(int): unique id of question
    question_str(str): question being asked
    tip(str): a tip to aid user
    _useful_in_topic(list): list of topic_ids where question can be used
    _useful_in_topic_name(list): list of topic_name where question may be used

    option_type(str): type of option the question has i.e either t/f or mcq
    option_selection(dict): selectable options each with an
    individual option_id and option_text
    selected_option_id(str): option_id of selected option
    to be derived from option_selection e.g option_selection['A'][1]
    correct_option(list): option_id of corrrect option
    status(str): status of question attempt by student i.e 'correct' or 'wrong'

    """
    def __init__(self, question_str, option_type, options=[], tip=None):
        ops = ['A', 'B', 'C', 'D', 'E']

        if not isinstance(question_str, str):
            raise TypeError('Invalid question text')
        else:
            self.question_str = question_str

        self.question_id = 'question_' + str(uuid4().int)

        if tip:
            if not isinstance(tip, str):
                raise TypeError('Invalid tip')
            else:
                self.tip = tip
        else:
            self.tip = ''

        self._useful_in_topic_id = []
        self._useful_in_topic_name = []

        self.option_selection = {}

        if not isinstance(options, list):
            raise TypeError('Options must be entered as a list')

        if not isinstance(option_type, str):
            raise TypeError('Invalid option type')
        elif option_type != 'mcq' and option_type != 't/f':
            raise TypeError('Invalid option type,  pls enter "mcq" or "t/f"')
        else:
            self.option_type = option_type

        if len(options) != 0:  # if options arg was entered
            if option_type == 't/f':
                raise ValueError('options arg not allowed for t/f option_type')
            elif option_type == 'mcq':
                if len(options) < 5 or len(options) > 5:
                    raise ValueError('Pls enter  5 options for mcq option_type')
                else:  # arrange pased option list as a dict
                    self.option_selection = dict(zip(ops, options))
                    """
                    for op in ops:
                        for option in options:
                            self.option_selection.update(
                                {op: [option, 'option_' + str(uuid4().int)]}
                            )
                    """
        else:  # options arg not entered
            if option_type == 't/f':
                self.option_selection = {
                    'True': [True, 'option_' + str(uuid4().int)],
                    'False': [False, 'option_' + str(uuid4().int)]
                }
            elif option_type == 'mcq':
                self.option_selection = {}

        self.selected_option = ''

        self.correct_option = ''

        self.status = ''


    @property
    def show_question(self):
        """Get the question with its options in a user friendly format"""
        self.reload()

        pretty_question = {'question': self.question_str}

        if self.option_type == 'mcq':
            if len(self.option_selection) == 0:
                pretty_option = {
                    'option_type': 'Multiple Choice Question',
                    'options': ['No option added, use edit_question() to add'],
                    'correct_option': ''
                }
            else:
                pretty_option = {
                    'option_type': 'Multiple Choice Question',
                    'options': [
                        self.option_selection['A'],
                        self.option_selection['B'],
                        self.option_selection['C'],
                        self.option_selection['D'],
                        self.option_selection['E']
                    ],
                    'correct_option': self.correct_option
                    # index 1 is the option_text
                }
        elif self.option_type == 't/f':
            if len(self.option_selection) == 0:
                pretty_option = {
                    'option_type': 'True or False Question',
                    'options': ['No option added, use edit_question() to add'],
                    'correct_option': ''
                }
            else:
                pretty_option = {
                    'option_type': 'True or False Question',
                    'options': [
                        self.option_selection['True'],
                        self.option_selection['False']
                    ],
                    'correct_option': self.correct_option
                }

        pretty_question.update(pretty_option)
        return pretty_question


    def edit_question(
            self,
            question_str,
            option_type,
            option_to_change=None,
            change_option_to=None,
    ):
        """
        Edit the attributes of an already existing questions object.
        Only one option can be changed at a time

        Args:
        question_str(str): new question string
        option_type(str): new_option_type. May be the same option
        type or a diff one
        option_to_change(str): A, B, C, D E. Only applicable if
        option_type is "mcq"
        change_option_to(str): replacement text for the selected option

        NOTE: Remember to call save() after any operation/edit is done
        this function does not save changes automatically to storage
        """
        self.reload()

        if not isinstance(question_str, str):
            raise TypeError('Invalid new question')
        else:
            self.question_str = question_str

        if not isinstance(option_type, str):
            raise TypeError('Invalid option type')
        elif option_type != 'mcq' and option_type != 't/f':
            raise ValueError('Invalid option type,  pls enter "mcq" or "t/f"')

        if option_type == 'mcq' and option_to_change is None:
            raise ValueError('An mcq option_type must be passed\
            with an option_to_change arg')

        if option_type == 'mcq' and change_option_to is None:
            raise ValueError('An mcq option_type must be passed with\
            a change_option_to arg')

        # Begin changing the question's option
        if self.option_type == 'mcq' and option_type == 't/f':
            # if the original option_type was mcq in storage but user wishes to
            # change it to 't/f'
            option_true = 'option_' + str(uuid4().int)
            option_false = 'option_' + str(uuid4().int)
            self.option_selection = {
                'True': [True, option_true],
                'False': [False, option_false]
            }
        elif option_type == 'mcq':
            # Same action will be performed on a t/f or mcq question in storage
            new_option_id = 'option_' + str(uuid4().int)
            if option_to_change == 'A':
                self.option_selection = {
                    'A': [change_option_to, new_option_id]
                }
            elif option_to_change == 'B':
                self.option_selection = {
                    'B': [change_option_to, new_option_id]
                }
            elif option_to_change == 'C':
                self.option_selection = {
                    'C': [change_option_to, new_option_id]
                }
            elif option_to_change == 'D':
                self.option_selection = {
                    'D': [change_option_to, new_option_id]
                }
            elif option_to_change == 'E':
                self.option_selection = {
                    'E': [change_option_to, new_option_id]
                }
            else:
                raise ValueError('Invalid option to change: Enter A - E')
        elif self.option_type == 't/f' and option_type == 't/f':
            # no changes to be done to the options of a t/f question
                pass


    def useful_in(self, get_ids=True):
        """
        Get the list of topic ids or names in which the question can be used in
        """
        if get_ids:
            return self._useful_in_topic_id
        else:
            return self._useful_in_topic_name

    def add_useful_in_topic(self, topic_id, topic_name):
        """
        Add an topic_id to the list of topic_ids where this ques
        tion object may be used

        Args:
        topic_id(str): id of topic to be added
        topic_name(str): nane of topic to be added

        """
        if not isinstance(topic_name, str) or not isinstance(topic_id, str):
            raise TypeError('Invalid topic credential(s)')

        self.reload()

        if topic_id not in self._useful_in_topic_id:
            self._useful_in_topic_id.append(topic_id)

        if topic_name not in self._useful_in_topic_name:
            self._useful_in_topic_name.append(topic_name)

    def reload(self):
        """Reload question obj attributes from storage"""
        # reload _useful_in_topic_name
        # reload _useful_in_topic_id
        pass  # remove when method is defined

    def save(self):
        """Save object to storage"""
            # Coming soon. . .
