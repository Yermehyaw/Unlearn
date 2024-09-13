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
    None

    Attributes:
    question_id(int): unique id of question
    question_str(str): question being asked
    tip(str): a tip to aid user
    useful_in_topic(list): list of topic_ids where question can be used
    useful_in_topic_name(list): list of topic_name where question may be used
    useful_in_lesson_id(list): ditto
    useful_in_lesson_name(list): ditto

    """
    def __init__(
            self,
            question_id,
            question_str,
            tip=None,
    ):
        if not isinstance(question_str, str):
            raise TypeError('Invalid question')
        else:
            self.question_str = question_str

        self.question_id = uuid4()

        if not isinstance(tip, str):
            raise TypeError('Invalid tip')
        else:
            self.tip = tip

        self.useful_in_lesson_id = []
        self.useful_in_lesson_name = []
        self.useful_in_topic_id = []
        self.useful_in_topic_name = []
