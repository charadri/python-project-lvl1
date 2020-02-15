# -*- coding:utf-8 -*-

"""Even game."""

from brain_games import cli
from brain_games.games import even


def main():
    """Run the game."""
    print('\nWelcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    user_name = cli.welcome_user()
    even.game(user_name)


if __name__ == '__main__':
    main()
