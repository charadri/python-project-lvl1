# -*- coding:utf-8 -*-

"""Prograssion game."""

import random


def game():
    """Provide."""
    begin = random.randint(1, 100)
    step = random.randint(1, 10)
    seq = make_seq(begin, step)
    answer = random.choice(seq)
    seq = hide_element(seq, answer)
    print('Question: ', end='')
    for element in seq:
        print(element, end=' ')
    print()
    return str(answer)


def make_seq(begin, step):
    """Make a sequence with first element (begin) and given step."""
    seq = []
    count = 0
    while count < 10:
        seq.append(begin + step * count)
        count += 1
    return seq


def hide_element(seq, element):
    """Hide element in sequence."""
    hide = seq.index(element)
    seq[hide] = '..'
    return seq
