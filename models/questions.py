#!/usr/bin/python3
"""
Question bank for the unlearn app

Modules Imported:
uuid4(method) - generate unique ids
UUID(cls) - base class for all uuid

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
    correct_option(str): option_id and option_text of the corrrect option

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
            raise TypeError('Invalid option type,  enter "mcq" or "t/f"')
        else:
            self.option_type = option_type

        self.option_selection = {}



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

            
