# -*- coding:utf-8 -*-

"""Greatest common divisor."""

import random


def give_rules():
    """Return game's rules.

    Returns:
        string: game rules.
    """
    return 'Find the greatest common divisor of given numbers.'


def give_q_and_a():
    """
    Return question and answer to it.

    Returns:
        question (string): two numbers.
        answer (string): greatest common divisor of given numbers.
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{x} {y}'.format(x=num1, y=num2)
    rest = 1
    while rest != 0:
        rest = int(num2) % int(num1)
        num2 = num1
        num1 = rest
    answer = str(num2)
    return question, answer
