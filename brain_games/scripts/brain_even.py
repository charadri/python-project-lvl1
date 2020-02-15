# -*- coding:utf-8 -*-

"""Even game."""

from brain_games import cli
from brain_games.games import run


def main():
    """Run the game."""
    print('\nWelcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    user_name = cli.welcome_user()
    run.even_game(user_name)


if __name__ == '__main__':
    main()
