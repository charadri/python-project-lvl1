# -*- coding:utf-8 -*-

"""Progression game."""

from brain_games import cli
from brain_games.games import run


def main():
    """Run the game."""
    print('\nWelcome to the Brain Games!')
    print('What number is missing in the progression?\n')
    user_name = cli.welcome_user()
    run.cycle(user_name, 'progress')


if __name__ == '__main__':
    main()
