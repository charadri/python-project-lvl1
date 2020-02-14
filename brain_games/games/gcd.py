# -*- coding:utf-8 -*-

"""Greatest common divisor."""

import random

from brain_games import functions


def game():
    """Provide."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print('Question: {x} {y}'.format(x=num1, y=num2))
    return functions.gcd(num1, num2)
