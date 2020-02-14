# -*- coding:utf-8 -*-

"""Progression game."""

from brain_games import cli
from brain_games.games import drive


def main():
    """Run the game."""
    user_name = cli.welcome_user('progress')
    drive.cycle(user_name, 'progress')


if __name__ == '__main__':
    main()
