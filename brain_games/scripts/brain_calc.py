# -*- coding:utf-8 -*-

"""Calculating game."""

from brain_games import cli
from brain_games.games import drive


def main():
    """Run the game."""
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?\n')
    user_name = cli.welcome_user()
    drive.cycle(user_name, 'calc')


if __name__ == '__main__':
    main()
