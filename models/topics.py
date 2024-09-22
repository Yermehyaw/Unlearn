#!/usr/bin/python3
"""
Topics under each course taken by student

Modules Imported:
uuid4(method) - generate unique ids
Courses(class) - create a course object
Lessons(class) - create a lesson object

"""
from uuid import uuid4
if __name__ == '__main__': # wanton but no need to change
    from lessons import Lessons  # from models.lessons . . . more preferrable
    from questions import Questions
else:
    from .lessons import Lessons
    from .questions import Questions


class Topics():
    """
    Create a topic under each course offered by a student

    Args:
    topic_title(str): title of the topic
    course_code(int): unique course code
    topic_desc(str): topic description (optional)
    topic_lecturer(str): name of lecturer taking the topic (optional)

    Attributes:
    topic_id(str): unique id of a topic
    lessons(list): list of all lessons the topic comprises
    course_code(int): unique course code
    topic_title(str): title of the topic
    course_title(str): name/title of course
    course_desc(str): course details
    topic_desc(str): topic description
    topic_lecturer(str): name of lecturer taking the topic
    questions(list): list of all question objs on the topic obj

    """
    def __init__(
            self,
            topic_title,
            course_code,
            topic_desc=None,
            topic_lecturer=None
    ):
        self.topic_id = 'topic_' + str(uuid4().int)

        self._lessons = []  # add to storageDB

        if not isinstance(course_code, int):
            raise TypeError('Invalid course code')
        else:
            self.course_code = course_code

        if not isinstance(topic_title, str):
            raise TypeError('Invalid topic title')
        else:
            self.topic_title = topic_title

        self.course_title = ''

        self.course_desc = ''

        self.topic_desc = ''
        if topic_desc:
            if not isinstance(topic_desc, str):
                raise TypeError('Invalid topic desc')
            else:
                self.topic_desc = topic_desc

        self.topic_lecturer = ''
        if topic_lecturer:
            if not isinstance(topic_lecturer, str):
                raise TypeError('Invalid lecturer name')
            else:
                self.topic_lecturer = topic_lecturer

        self.questions = []

    @property
    def all_topics_no(self):
        """Returns the total no of topics"""
        # use self.reload() to retrieve from db or storage would handle this
        return Topics.no_topics

    @property
    def lessons(self):
        """Property getter of lessons attr"""
        return self._lessons

    @lessons.setter
    def lessons(self, new_lessson):
        """
        Property setter of lessons attr

        Args:
        _dict(dict): dictionary of Lessons obj details to be added to lessons
        """
        if not isinstance(new_lessson, Lessons):
            raise TypeError('Invalid lesson name')
        else:
            self._lessons.append(new_lessson)

    def add_lesson(self, lesson_title, lesson_content, lesson_desc=None):
        """
        Adds a new Lessons object to a Topics object
        Crucial in storageDB
        """
        new_lessson = Lessons(lesson_title, lesson_content, lesson_desc)
        self.lessons = new_lessson

        # add the created Lessons() obj to storage

    def add_questions(self, question_str, option_type):
        """Create a question obj on the topic obj"""
        new_question = Questions(question_str, option_type)
        self.questions.append(new_question)
        # Save to storage
        return new_question
