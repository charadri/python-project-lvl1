# -*- coding:utf-8 -*-

"""Even game."""

import random

from brain_games import functions


def game():
    """Provide a little game logic."""
    number = random.randint(1, 100)
    print('Question: {x}'.format(x=number))
    return functions.even(number)
