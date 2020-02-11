# -*- coding:utf-8 -*-

"""Even game."""

from random import randint

from brain_games import cli


def is_even(number):
    """
    Check number for parity.

    Returns:
    'yes' if number is even
    'no' in otherwise

    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def game(user_name):
    """Provide a little game logic."""
    count = 0
    win = True
    while count < 3:
        number = randint(1, 100)
        print('Question: {x}'.format(x=number))
        answer = input('Your answer: ')
        correct_answer = is_even(number)
        if answer == correct_answer:
            cli.correct_answer()
        else:
            cli.wrong_answer(answer, correct_answer, user_name)
            win = False
            break
        count += 1
    if win:
        print('Congratulations, {name}!'.format(name=user_name))
