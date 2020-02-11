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
    win = False
    while count < 3:
        number = randint(1, 100)
        print('Question: {x}'.format(x=number))
        try:
            answer = input('Your answer: ')
        except EOFError:
            print('\nSee ya!')
            break
        except KeyboardInterrupt:
            print('\nSee ya!')
            break
        else:
            correct_answer = is_even(number)
            if answer == correct_answer:
                cli.correct_answer()
                win = True
            else:
                cli.wrong_answer(answer, correct_answer, user_name)
                break
            count += 1
    if win:
        print('Congratulations, {name}!'.format(name=user_name))
