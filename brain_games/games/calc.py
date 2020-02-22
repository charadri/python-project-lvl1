# -*- coding:utf-8 -*-

"""Calculating game."""

import random


def get_rules():
    """Return game's rules.

    Returns:
        string: game rules.
    """
    return 'What is the result of the expression?'


def get_q_and_a():
    """Return question and asnwer to it.

    Returns:
        question (string): expression to calculate.
        answer (string): result of calculation.
    """
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = '{a} {op} {b}'.format(a=first_num, op=operation, b=second_num)
    if operation == '+':
        answer = str(first_num + second_num)
    elif operation == '-':
        answer = str(first_num - second_num)
    else:
        answer = str(first_num * second_num)
    return question, answer
