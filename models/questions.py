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
    tip(str): a tip to aid user
    option_type(str): type of option the question has i.e either mcq or t/f

    Attributes:
    question_id(int): unique id of question
    question_str(str): question being asked
    tip(str): a tip to aid user
    _useful_in_topic(list): list of topic_ids where question can be used
    _useful_in_topic_name(list): list of topic_name where question may be used

    option_type(str): type of option the question has i.e either t/f or mcq
    option_selection(dict): selectable options each with an
    individual option_id and option_text
    selected_option(list): option_id and option_text of the selected option
    correct_option(list): option_id and option_text of the corrrect option

    """
    def __init__(self, question_str, tip=None):
        if not isinstance(question_str, str):
            raise TypeError('Invalid question')
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

        if not isinstance(option_type, str):
            raise TypeError('Invalid option type')
        elif option_type != 'mcq' or option_type != 't/f':
            raise TypeError('Invalid option type,  pls enter "mcq" or "t/f"')
        else:
            self.option_type = option_type

        self.option_selection = {}

        self.selected_option = []

        self.correct_option = []


    @property
    def show_question(self):
        """Get the question with its options in a user friendly format"""
        self.reload()

        pretty_question = {'question': question_str}

        if self.option_type == 'mcq':
            pretty_option = {
                'option_type': 'Multiple Choice Question',
                'options': [
                    self.option_selection['A'],
                    self.option_selection['B'],
                    self.option_selection['C'],
                    self.option_selection['D'],
                    self.option_selection['E']
                ],
                'correct_option': self.correct_option[1]
                # index 1 is the option_text
            }
        elif self.option_type == 't/f':
            pretty_option = {
                'option_type': 'True or False Question',
                'options': [
                    self.option_selection['True'],
                    self.option_selection['False']
                ],
                'correct_option': self.correct_option[1]
            }

        final_pretty_q = pretty_question.update(pretty_option)
        return final_pretty_q


    @show_question.setter
    def edit_question(
            self,
            question_str,
            option_type,
            option_to_change,
            change_option_to,
    ):
        """
        Edit the attributes of an already existing questions object

        Args:
        question_str(str): new question string
        option_type(str): new_option_type. May be the same option
        type or a diff one
        option_to_change(str): A, B, C, D E. Only applicable if
        option_type is "mcq"
        change_option_to(str): string to change the selected option into

        NOTE: Remember to call sace() after any operation/edit is dobe
        this function does not save changes automatically to storage
        """
        self.reload()

        if not isinstance(question_str, str):
            raise TypeError('Invalid new question')
        else:
            self.question_str = question_str

        if self.option_type == 'mcq' and option_type == 't/f':
            # if the original option_type was mcq but user wishes to
            # change it to 't/f'
            option_true = 'option_' + str(uuid4().int)
            option_false = 'option_' + str(uuid4().int)
            self.option_selection = {
                'True': [True, option_true],
                'False': [False, option_false]
            }
        elif self.option_type == 't/f' and option_type == 'mcq':
            # if the original option_type was t/f but now being changed
            # to mcq
            new_option_id = 'option_' + str(uuid4().int)

            if option_to_change == 'A':  # use switch case statement
                self.option_selection = {
                    'A': [change_option_to, new_option_id]
                }
            elif option_to_change == 'B':
                # continue from here

        elif self.option_type == 'mcq' and option_type == 'mcq':

        elif self.option_type == 't/f' and option_type == 't/f':
                pass

    def useful_in(self, get_ids=True):
        """
        Get the list of topic ids or nanes in which the question can be used in
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
