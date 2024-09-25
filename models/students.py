#!/usr/bin/python3
"""
Student class from which defines all student users

Modules Imported:
bcrypt(func) - encrypt a password string
uuid4(method) - Generates a random UUID
"""
import bcrypt
from datetime import datetime
from uuid import uuid4


class Students():
    """
    Defines a student user

    Args:
    name(str): student name
    username: login username
    password(str): login password

    Attributes:
    student_id(str): unique student id
    name(str): student's name
    username(str): login username
    study_year(int): year of study (Not added yet)
    p_hash(str): hash value of password
    created_at(timestamp): timestamp when student user was created

    """
    def __init__(self, username, password, name=None):
        """Class initializer"""
        self.student_id = 'student_' + str(uuid4().int)

        self.name = name
        if name:
            if not isinstance(name, str):
                raise TypeError('Enter a valid name')
            else:
                self.name = name

        if not isinstance(username, str):
            raise TypeError('Enter a valid username')
        else:
            self.username = username

        if username:  # == any username already in storage
            pass  # when storage_db is added, print("username already exists")

        __salt = bcrypt.gensalt()
        self.p_hash = bcrypt.hashpw(password.encode('utf-8'), __salt)

        self.created_at = datetime.now()

    def to_dict(self):
        """Repeesent instance as a dict for json storage"""
        dict = {}
        dict.update(self.__dict__)
        dict.update({'__class__': 'Students'})
        return dict
