# -*- coding:utf-8 -*-

"""Calculating game."""

import random


def give_answer():
    """
    Return answer to question.

    Returns:
        Result of a calculation as a string.
    """
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    oper = random.choice(['+', '-', '*'])
    print('Question: {a} {op} {b}'.format(a=first_num, op=oper, b=second_num))
    return calc(first_num, second_num, oper)


def calc(num1, num2, operation):
    """
    Calculate the value of an expression.

    Args:
        num1 (int): first number.
        num2 (int): second number.
        operation (string): operation sign.

    Returns:
        string: result of an operation.
    """
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    return str(num1 * num2)


def ask_question():
    """Print game's rules."""
    print('What is the result of the expression?')
    print()
