# -*- coding:utf-8 -*-

"""Calculating game."""

import random

from brain_games import functions


def game():
    """Provide a little game logic."""
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    oper = random.choice(['+', '-', '*'])
    print('Question: {a} {op} {b}'.format(a=first_num, op=oper, b=second_num))
    return functions.calc(first_num, second_num, oper)
