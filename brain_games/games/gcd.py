# -*- coding:utf-8 -*-

"""Greatest common divisor."""

import random


def game():
    """Return answer to a question."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print('Question: {x} {y}'.format(x=num1, y=num2))
    return gcd(num1, num2)


def gcd(num1, num2):
    """Find the greatest common divisor of two numbers."""
    rest = 1
    while rest != 0:
        rest = int(num2) % int(num1)
        num2 = num1
        num1 = rest
    return str(num2)
