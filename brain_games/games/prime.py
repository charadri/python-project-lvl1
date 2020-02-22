# -*- coding:utf-8 -*-

"""Prime game."""

import random


def get_rules():
    """Return game's rules.

    Returns:
        string: game rules.
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_q_and_a():
    """
    Return answer to a question.

    Returns:
        question (int): number from 1 to 100.
        answer (string): 'yes' if number is prime, 'no' otherwise.
    """
    number = random.randint(1, 100)
    question = number
    is_prime = True
    count = 2
    while count <= number // 2:
        if int(number) % count == 0:
            is_prime = False
        count += 1
    if is_prime:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
