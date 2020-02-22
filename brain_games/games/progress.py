# -*- coding:utf-8 -*-

"""Prograssion game."""

import random


def get_rules():
    """Return game's rules.

    Returns:
        string: game rules.
    """
    return 'What number is missing in the progression?'


def get_q_and_a():
    """
    Return answer to a question.

    Returns:
        question (string): sequence with hidden element.
        answer (string): hidden element of the sequence.
    """
    begin = random.randint(1, 100)
    step = random.randint(1, 10)
    seq = make_seq(begin, step)
    answer = random.choice(seq)
    seq = hide_element(seq, answer)
    question = ' '
    question = question.join(seq)
    return question, answer


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
        element = str(begin + step * count)
        seq.append(element)
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
