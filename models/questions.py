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
    None

    Attributes:
    question_id(int): unique id of question
    question_str(str): question being asked
    tip(str): a tip to aid user
    useful_in_topic(list): list of topic_ids where question can be used
    useful_in_topic_name(list): list of topic_name where question may be used

    """
    def __init__(self, question_str, tip=None):
        if not isinstance(question_str, str):
            raise TypeError('Invalid question')
        else:
            self.question_str = question_str

        self.question_id = uuid4()

        if tip:
            if not isinstance(tip, str):
                raise TypeError('Invalid tip')
            else:
                self.tip = tip

        self._useful_in_topic_id = []
        self._useful_in_topic_name = []

    @property
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
        topic_id(uuid): id of topic to be added
        topic_name(str): nane of topic to be added

        """
        if not isinstance(topic_name, str):
            raise TypeError('Invalid topic name')

        self.reload()

        if topic_id not in self._useful_in_topic_id:
            self._useful_in_topic_id.append(topic_id)

        if topic_name not in self._useful_in_topic_name:
            self._useful_in_topic_name.append(topic_name)

    def reload(self):
        """Reload question obj attributes from storage"""
        # reload _useful_in_topoc_nanrle
        # reload _useful_in_topic_id
        pass  #:remove when method is defined

    def save(self):
        """Save object to storage"""
            # Coming soon. . .
