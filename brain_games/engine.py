# -*- coding:utf-8 -*-

"""Main cycle for games."""

from brain_games import cli


def run(game):
    """
    Run the game.

    Args:
        game: name of the module with game logic.
    """
    print()
    print('Welcome to the Brain Games!')
    game.ask_question()
    user_name = cli.welcome_user()
    win = True
    count = 0
    while count < 3:
        correct_answer = game.give_answer()
        answer = input('Your answer: ')
        if answer == correct_answer:
            cli.correct_answer()
        else:
            cli.wrong_answer(answer, correct_answer, user_name)
            win = False
            break
        count += 1
    if win:
        print('Congratulations, {name}!'.format(name=user_name))
