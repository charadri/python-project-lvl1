# -*- coding:utf-8 -*-

"""Divisor game."""

from brain_games import cli
from brain_games.games import drive


def main():
    """Run the game."""
    print('\nWelcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.\n')
    user_name = cli.welcome_user()
    drive.cycle(user_name, 'gcd')


if __name__ == '__main__':
    main()
