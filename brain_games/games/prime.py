# -*- coding:utf-8 -*-

"""Prime game."""

import random


def give_answer():
    """
    Return answer to a question.

    Returns:
        'yes' (string): if number is prime
        'no' (string): in otherwise
    """
    number = random.randint(1, 100)
    print('Question: {x}'.format(x=number))
    count = 2
    while count <= number // 2:
        if int(number) % count == 0:
            return 'no'
        count += 1
    return 'yes'


def ask_question():
    """Print games' rules."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print()
