# -*- coding:utf-8 -*-

"""Greatest common divisor."""

import random


def get_rules():
    """Return game's rules.

    Returns:
        string: game rules.
    """
    return 'Find the greatest common divisor of given numbers.'


def get_q_and_a():
    """
    Return question and answer to it.

    Returns:
        question (string): two numbers.
        answer (string): greatest common divisor of given numbers.
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{x} {y}'.format(x=num1, y=num2)
    answer = str(gcd(num1, num2))
    return question, answer


def gcd(num1, num2):
    """Return greatest common divisor of two numbers.

    Args:
        num1 (int): first number.
        num2 (int): second number.

    Returns:
        int: greatest common divisor.
    """
    rest = 1
    while rest != 0:
        rest = int(num2) % int(num1)
        num2 = num1
        num1 = rest
    return num2
