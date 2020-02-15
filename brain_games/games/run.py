# -*- coding:utf-8 -*-

"""Main cycle for games."""


from brain_games import cli
from brain_games.games import calc, even, gcd, prime, progress


def cycle(user_name, game_name):
    """Provide a little game logic."""
    count = 0
    while count < 3:
        correct_answer = game_name.game()
        answer = cli.give_answer()
        check_answer(answer, correct_answer, user_name)
        count += 1
    print('Congratulations, {name}!'.format(name=user_name))


def check_answer(answer, correct_answer, user_name):
    """Check user's answer."""
    if answer == correct_answer:
        cli.correct_answer()
    else:
        cli.wrong_answer(answer, correct_answer, user_name)
        exit(0)


def calc_game(user_name):
    """Run calc game."""
    cycle(user_name, calc)


def even_game(user_name):
    """Run even game."""
    cycle(user_name, even)


def gcd_game(user_name):
    """Run gcd game."""
    cycle(user_name, gcd)


def progress_game(user_name):
    """Run progression game."""
    cycle(user_name, progress)


def prime_game(user_name):
    """Run prime game."""
    cycle(user_name, prime)
