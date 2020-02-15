# -*- coding:utf-8 -*-

"""Progression game."""

from brain_games import cli
from brain_games.games import progress


def main():
    """Run the game."""
    print('\nWelcome to the Brain Games!')
    print('What number is missing in the progression?\n')
    user_name = cli.welcome_user()
    progress.game(user_name)


if __name__ == '__main__':
    main()
