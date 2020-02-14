# -*- coding:utf-8 -*-

"""Main cycle for games."""


from brain_games import cli
from brain_games.games import calc, even, gcd, prime, progress


def cycle(user_name, game_name):
    """Provide a little game logic."""
    count = 0
    while count < 3:
        correct_answer = run(game_name)
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


def run(name):
    """Run the iteration of game."""
    games = {
        'even': even.game,
        'calc': calc.game,
        'gcd': gcd.game,
        'prime': prime.game,
        'progress': progress.game,
        }
    return games[name]()
