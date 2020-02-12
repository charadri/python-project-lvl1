# -*- coding:utf-8 -*-

"""Main cycle for games."""


from brain_games import cli
from brain_games.games import calc, even


def cycle(user_name, game_name):
    """Provide a little game logic."""
    count = 0
    while count < 3:
        if game_name == 'even':
            correct_answer = even.game()
        elif game_name == 'calc':
            correct_answer = calc.game()
        answer = cli.give_answer()
        if answer == correct_answer:
            cli.correct_answer()
            win = True
        else:
            cli.wrong_answer(answer, correct_answer, user_name)
            win = False
            break
        count += 1
    if win:
        print('Congratulations, {name}!'.format(name=user_name))
