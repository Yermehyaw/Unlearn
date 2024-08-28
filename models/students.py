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
    student_id(int): unique student id
    name(str): student's name
    username(str): login username
    p_hash(str): hash value of password
    created_at(timestamp): timestamp when student user was created
    """
    def __init__(self, name=None, username, password):
        """
        Class initializer
        """
        self.student_id = uuid4()
        if not isinstance(name, str) or not isinstance(username, str):
            raise TypeError('Enter a valid name')
        else:
            self.name = name
            self.username = username

        if username:  # == any username already in storage
            pass  # when storage_db is added, print("username already exists")

        __salt = bcrypt.gensalt()
        self.p_hash = bcrypt.hashpw(password.encode('utf-8'), __salt)

        self.created_at = datetime.now()
