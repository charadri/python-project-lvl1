# -*- coding:utf-8 -*-

"""Calculating game."""

import random
from brain_games.games import run


def game(user_name):
    """"""
    run.cycle(user_name, 'calc')


def answer():
    """Provide a little game logic."""
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    oper = random.choice(['+', '-', '*'])
    print('Question: {a} {op} {b}'.format(a=first_num, op=oper, b=second_num))
    return calc(first_num, second_num, oper)


def calc(num1, num2, operator):
    """Calculate the value of an expression."""
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    return str(num1 * num2)
