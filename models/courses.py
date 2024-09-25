#!/usr/bin/python3
"""
Courses offered by student

Modules Imported:
Topics: topics under each course

"""
if __name__ == '__main__':
    from topics import Topics
else:
    from .topics import Topics


class Courses:
    """
    Create a course object representing a course offered by students

    Args:
    course_code(int): unique course code
    course_title(str): name/title of course
    course_desc(str): course details

    Attributes:
    course_code(int): unique course code
    course_title(str): name/title of course
    course_desc(str): course details/description
    _no_topics(int): no of topics in the course
    _all_topics(list): list of all topic objs in course

    """
    def __init__(self, course_code, course_title=None, course_desc=None):
        """Course object initializer"""
        self._no_topics = 0
        self._all_topics = []
        if not isinstance(course_code, int):
            raise TypeError('Invalid course code')
        else:
            self.course_code = course_code

        self.course_title = ''
        if course_title:
            if not isinstance(course_title, str):
                raise TypeError('Invalid course title')
            else:
                self.course_title = course_title

        self.course_desc = ''
        if course_desc:
            if not isinstance(course_desc, str):
                raise TypeError('Invalid course desc')
            else:
                self.course_desc = course_desc

    @property
    def get_topics_no(self):
        """Returns the no of topics in each course"""
        # retrieve no_topocs from db
        return self._no_topics

    @property
    def get_all_topics_list(self):
        """Returns a list of all topics in the course"""
        # retrieve from db
        return self._all_topics

    def add_topic(self, new_topic_title, new_cs_code=None):
        """Creates a new topic"""
        new_topic = Topics(new_topic_title, self.course_code)

        self._no_topics += 1

        self._all_topics.append(new_topic.topic_title)

        return new_topic

    def to_dict(self):
        """Repeesent instance as a dict for json storage"""
        dict = {}
        dict.update(self.__dict__)
        dict.update({'__class__': 'Courses'})
        return dict
