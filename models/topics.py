#!/usr/bin/python3
"""
Topics under each course taken by student

Modules Imported:
uuid4(method) - generate unique ids
Courses(class) - create a course object
Lessons(class) - create a lesson object

"""
from uuid import uuid4
if __name__ == '__main__':
    from courses import Courses
    from lessons import Lessons
else:
    from .courses import Courses
    from .lessons import Lessons


class Topics(Courses):
    """
    Create a topic under each course offered by a student

    Args:
    course_code(int): unique course code
    topic_title(str): title of the topic
    course_title(str): name/title of course (optional)
    course_desc(str): course details (optional)
    topic_desc(str): topic description (optional)

    Attributes:
    topic_id(int): unique id of a topic
    lessons(list): list of all lessons the topic comprises
    course_code(int): unique course code
    topic_title(str): title of the topic
    course_title(str): name/title of course
    course_desc(str): course details
    topic_desc(str): topic description
    topic_lecturer(str): name of lecturer taking the topic

    """
    def __init__(
            self,
            course_code,
            topic_title,
            course_title=None,
            course_desc=None,
            topic_desc=None,
            topic_lecturer=None
    ):
        super().__init__(course_code, course_title, course_desc)

        self.topic_id = uuid4()

        self._lessons = []  # add to storageDB

        if not isinstance(topic_title, str):
            raise TypeError('Invalid topic title')
        else:
            self.topic_title = topic_title

        self.topic_desc = topic_desc
        if topic_desc:
            if not isinstance(topic_desc, str):
                raise TypeError('Invalid topic desc')
            else:
                self.topic_desc = topic_desc

        if not isinstance(topic_lecturer, str):
            raise TypeError('Invalid lecturer name')
        else:
            self.topic_lecturer = topic_lecturer

    @property
    def lessons(self):
        """Property getter of lessons attr"""
        return self._lessons

    @lessons.setter
    def lessons(self, _dict):
        """
        Property setter of lessons attr

        Args:
        _dict(dict): dictionary of Lessons obj details to be added to lessons
        """
        if not isinstance(_dict, dict):
            raise TypeError('Lesson details must be passed as a dict')
        else:
            self._lessons.append(_dict)

    def add_lesson(self, lesson_title, lesson_content, lesson_desc=None):
        """
        Adds a new Lessons object to a Topics object
        Crucial in storageDB
        """
        lesson = Lessons(lesson_title, lesson_content, lesson_desc)
        lesson_details = {}

        lesson_details['lesson_obj'] = lesson  # may not be necessary
        lesson_details['lesson_id'] = lesson.lesson_id
        lesson_details['lesson_title'] = lesson.lesson_title
        lesson_details['lesson_content'] = lesson.lesson_content
        lesson_details['lesson_desc'] = lesson.lesson_desc

        lessons = lesson_details
