#!/usr/bin/python3
"""
JSON file storage for Unlearn web app

Modules Imported:
json: serialize and deserialize json file_storage

"""
import json


class FileStorage:
    """Handles storage needs of web app via JSON"""
    __file_path = 'unlearn_storage.json'
    __objects = {}

    def all(self):
        """Loads all objects from staorge"""

    def new(self, obj):
        """Adds new object to storage dict i.e __objects"""

    def save(self):
        """Commits new objects in __objects to json storage i.e unlearn_storage.json"""

    def reload(self):
        """Loads committed objects from json storage"""

