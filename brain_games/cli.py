# -*- coding:utf-8 -*-

"""CLI interactions."""

import prompt


def bye():
    """Says goodbye."""
    print('\nSee ya!')
    exit(0)


def welcome_user(game=None):
    """
    Welcomes user.

    Greeting user and returns his name.

    Returns:
    string:user's name

    """
    print('\nWelcome to the Brain Games!')
    if game == 'even':
        print('Answer "yes" if number even otherwise answer "no".\n')
    elif game == 'calc':
        print('What is the result of the expression?\n')
    elif game == 'gcd':
        print('Find the greatest common divisor of given numbers.\n')
    elif game == 'progress':
        print('What number is missing in the progression?\n')
    elif game == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no"\n')
    return give_name()


def give_name():
    """Recieve a user's name."""
    try:
        name = prompt.string('May I have your name? ')
    except EOFError:
        bye()
    except KeyboardInterrupt:
        bye()
    print('Hello, {name}!\n'.format(name=name))
    return name


def give_answer():
    """Recieve an answer from user."""
    try:
        return input('Your answer: ')
    except EOFError:
        bye()
    except KeyboardInterrupt:
        bye()


def correct_answer():
    """In case of correct answer."""
    print('Correct!')


def wrong_answer(user_answer, correct, user_name):
    """
    In case of wrong answer.

    Parameters:
    user_answer (string): user's answer
    correct (string): correct answer
    user_name (string): user's name

    """
    print("'{answer}' is wrong answer ;(.".format(answer=user_answer), end=' ')
    print("Correct answer was '{answer}'.".format(answer=correct))
    print("Let's try again, {name}!".format(name=user_name))
