# -*- coding:utf-8 -*-

"""Fucntions for games."""

import random


def even():
    """
    Check the number for parity.

    Returns:
    'yes' (string): if number is even
    'no' (string): in otherwise

    """
    number = random.randint(1, 100)
    print('Question: {x}'.format(x=number))
    if number % 2 == 0:
        return 'yes'
    return 'no'


def calc():
    """Calculate the value of an expression."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    print('Question: {a} {oper} {b}'.format(a=num1, oper=operator, b=num2))
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num2 - num2)
    return str(num1 * num2)
