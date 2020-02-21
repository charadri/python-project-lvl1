# -*- coding:utf-8 -*-

"""Greatest common divisor."""

import random


def give_answer():
    """
    Return answer to a question.

    Returns:
        Greatest common divisor of two numbers as a string.
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print('Question: {x} {y}'.format(x=num1, y=num2))
    return gcd(num1, num2)


def gcd(num1, num2):
    """
    Find the greatest common divisor of two numbers.

    Args:
        num1: first number
        num2: second number

    Returns:
        string: greatest common divisor of two numbers.
    """
    rest = 1
    while rest != 0:
        rest = int(num2) % int(num1)
        num2 = num1
        num1 = rest
    return str(num2)


def ask_question():
    """Print game's rules."""
    print('Find the greatest common divisor of given numbers.')
    print()
