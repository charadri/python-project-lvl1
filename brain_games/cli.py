# -*- coding:utf-8 -*-

"""CLI interactions."""

import prompt


def welcome_user():
    """
    Welcomes user.

    Returns:
        string: user's name
    """
    user_name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=user_name))
    print()
    return user_name


def correct_answer():
    """In case of correct answer."""
    print('Correct!')


def wrong_answer(user_answer, correct, user_name):
    """
    In case of wrong answer.

    Args:
        user_answer (string): user's answer
        correct (string): correct answer
        user_name (string): user's name

    """
    print("'{answer}' is wrong answer ;(.".format(answer=user_answer), end=' ')
    print("Correct answer was '{answer}'.".format(answer=correct))
    print("Let's try again, {name}!".format(name=user_name))
