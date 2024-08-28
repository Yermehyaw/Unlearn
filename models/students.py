#!/usr/bin/python3
"""
Student class from which defines all student users

Modules Imported:
bcrypt(func) - encrypt a password string
uuid4(method) - Generates a random UUID
"""
import bcrypt
from datetime import datetime
from uuid import uuid4  # funtion


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
        student_id = uuid4()
        name = name

        if not username:  # username is None
            raise ValueError('Pls enter a valid username')
        else if username:  # == any username already in storage
            pass  # when storage_db is added, print("username already exists")

        __salt = bcrypt.gensalt()
        p_hash = bcrypt.hashpw(password.encode('utf-8'), __salt)

        created_at = datetime.now()
