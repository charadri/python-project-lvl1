# -*- coding:utf-8 -*-

"""Divisor game."""

from brain_games import cli
from brain_games.games import gcd


def main():
    """Run the game."""
    print('\nWelcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.\n')
    user_name = cli.welcome_user()
    gcd.game(user_name)


if __name__ == '__main__':
    main()
