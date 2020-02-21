# -*- coding:utf-8 -*-

"""Even game."""

import random


def give_answer():
    """Return answer to a question.

    Returns:
        'yes' (string): if number is even
        'no' (string): in otherwise
    """
    number = random.randint(1, 100)
    print('Question: {x}'.format(x=number))
    if number % 2 == 0:
        return 'yes'
    return 'no'


def ask_question():
    """Print game's rules."""
    print('Answer "yes" if number even otherwise answer "no".')
    print()
