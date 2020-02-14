# -*- coding:utf-8 -*-

"""Fucntions for games."""


def even(number):
    """
    Check the number for parity.

    Returns:
    'yes' (string): if number is even
    'no' (string): in otherwise

    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def calc(num1, num2, operator):
    """Calculate the value of an expression."""
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    return str(num1 * num2)


def gcd(num1, num2):
    """Find the greatest common divisor of two numbers."""
    rest = 1
    while rest != 0:
        rest = int(num2) % int(num1)
        num2 = num1
        num1 = rest
    return str(num2)
