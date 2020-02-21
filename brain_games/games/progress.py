# -*- coding:utf-8 -*-

"""Prograssion game."""

import random


def give_answer():
    """
    Return answer to a question.

    Returns:
        string: hidden number in a sequence.
    """
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
    """
    Make a sequence with first element (begin) and given step.

    Args:
        begin (int): first number is sequence.
        step (int): step in arithmetic progression.

    Returns:
        list: arithmetic progression of 10 elements with given step.
    """
    seq = []
    count = 0
    while count < 10:
        seq.append(begin + step * count)
        count += 1
    return seq


def hide_element(seq, element):
    """
    Hide element in sequence.

    Args:
        seq (list): sequence of numbers.
        element (int): element to hide.

    Returns:
        list: sequence with hidden element.
    """
    hide = seq.index(element)
    seq[hide] = '..'
    return seq


def ask_question():
    """Print game's rules."""
    print('What number is missing in the progression?')
    print()
