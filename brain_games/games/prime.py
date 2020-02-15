# -*- coding:utf-8 -*-

"""Prime game."""

from random import randint


def game():
    """Return answer to a question."""
    number = randint(1, 100)
    print('Question: {x}'.format(x=number))
    return is_prime(number)


def is_prime(number):
    """Check the number for prime."""
    count = 2
    while count <= number // 2:
        if int(number) % count == 0:
            return 'no'
        count += 1
    return 'yes'
