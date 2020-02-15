# -*- coding:utf-8 -*-

"""Main cycle for games."""


from brain_games import cli
from brain_games.games import calc, even, gcd, prime, progress


def cycle(user_name, game_name):
    """Provide a little game logic."""
    count = 0
    while count < 3:
        correct_answer = give_answer(game_name)
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


def give_answer(name):
    games = {
        'even': even.answer,
        'calc': calc.answer,
        'gcd': gcd.answer,
        'progress': progress.answer,
        'prime': prime.answer,
        }
    return games[name]()
