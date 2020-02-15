# -*- coding:utf-8 -*-

"""Calculating game."""

from brain_games import cli
from brain_games.games import calc


def main():
    """Run the game."""
    print('\nWelcome to the Brain Games!')
    print('What is the result of the expression?\n')
    user_name = cli.welcome_user()
    calc.game(user_name)


if __name__ == '__main__':
    main()
