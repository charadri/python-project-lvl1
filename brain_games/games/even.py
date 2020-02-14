# -*- coding:utf-8 -*-

"""Even game."""

import random


def game():
    """Provide a little game logic."""
    number = random.randint(1, 100)
    print('Question: {x}'.format(x=number))
    return is_even(number)


def is_even(number):
    """
    Check the number for parity.

    Returns:
    'yes' (string): if number is even
    'no' (string): in otherwise

    """
    if number % 2 == 0:
        return 'yes'
    return 'no'
