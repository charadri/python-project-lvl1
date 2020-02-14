# -*- coding:utf-8 -*-

"""Divisor game."""

from brain_games import cli
from brain_games.games import drive


def main():
    """Run the game."""
    user_name = cli.welcome_user('gcd')
    drive.cycle(user_name, 'gcd')


if __name__ == '__main__':
    main()
