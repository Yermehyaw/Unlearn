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

    def load_all(self):
        """Loads all objects from staorge"""
        return FileStorage.__objects

    def add(self, obj):
        """Adds new object to storage dict i.e __objects awaiting commit
        to json file
        """
        FileStorage.__objects.update(
                {obj.to_dict()['__class__']
                 + '.'
                 +  obj.id: obj}
        )

    def save(self):
        """Commits new objects in __objects to json storage
        i.e unlearn_storage.json"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads committed objects from json storage"""
        from models.courses import Courses
        from models.lessons import Lessons
        from models.questions import Questions
        from models.result import Result
        from models.students import Students
        from models.topics import Topics


        classes = {
                'Courses': Courses, 'Lessons': Lessons, 'Questions': Questions,
            'Quiz': Lessons.Quiz, 'Result': Result, 'Students': Students,
            'Topics': Topics
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)

            for key, value in temp.items():
                all_objs = self.load_all()  # all_objs auto updates __objects
                all_objs[key] = classes[value['__class__']](**value)
                # **value inits all the saved obj attr to their respective keys

        except FileNotFoundError:
            pass
