#!/usr/bin/python3
"""
Marks a list of question objects

Modules Imported:
Questions(cls): Questions class

"""
if __name__ == '__main__':
    from questions import Questions
else:
    from models.questions import Questions


def marker(user_attempts):
    """
    Marks a list of question objects

    Args:
    user_attempts(list): a list of question objects

    Return:
    a marked user_attempts

    """
    if not isinstance(user_attempts, list):
        raise TypeError('Invalid arg: user_attempts must be a list')
    elif not isinstance(user_attempts[0], Questions):
        raise TypeError('Only Questions obj are allowed')

    for question in user_attempts:
        selected_option_id = question.selected_option[1]
        correct_option_id = question.correct_option[1]
        if len(question.selected_option_id) > 0:
            if question.selected_option_id == self.correct_option_id:
                question.status = 'correct'
            elif question.selected_option_id != self.correct_option_id:
                question.status = 'wrong'
        else:
            question.status = 'unanswered'

    return user_attempts
