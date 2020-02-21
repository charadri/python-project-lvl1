# -*- coding:utf-8 -*-

"""Even game."""

import random


def give_rules():
    """Return game's rules.

    Returns:
        string: game rules.
    """
    return 'Answer "yes" if number even otherwise answer "no".'


def give_q_and_a():
    """Return question and answer to it.

    Returns:
        question (int): number from 1 to 100.
        answer (string): 'yes' if number is even, 'no' otherwise.
    """
    number = random.randint(1, 100)
    question = number
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
