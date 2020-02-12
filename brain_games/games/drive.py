# -*- coding:utf-8 -*-

"""Main cycle for games."""

from brain_games import cli, functions


def cycle(user_name, game_name):
    """Provide a little game logic."""
    count = 0
    while count < 3:
        if game_name == 'even':
            correct_answer = functions.even()
        elif game_name == 'calc':
            correct_answer = functions.calc()
        try:
            answer = input('Your answer: ')
        except EOFError:
            print('\nSee ya!')
            break
        except KeyboardInterrupt:
            print('\nSee ya!')
            break
        else:
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
