# -*- coding:utf-8 -*-

"""Main cycle for games."""

from brain_games import cli

ROUNDS = 3


def run(game):
    """
    Run the game.

    Args:
        game: name of the module with game logic.
    """
    print()
    print('Welcome to the Brain Games!')
    print(game.get_rules())
    print()
    user_name = cli.welcome_user()
    count = 1
    while count <= ROUNDS:
        question, correct_answer = game.get_q_and_a()
        print('Question: {q}'.format(q=question))
        answer = input('Your answer: ')
        if answer == correct_answer:
            cli.approve_answer()
        else:
            cli.reject_answer(answer, correct_answer, user_name)
            break
        count += 1
    else:
        cli.congratulate(user_name)
