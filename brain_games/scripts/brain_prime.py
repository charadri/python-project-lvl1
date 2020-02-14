# -*- coding:utf-8 -*-

"""Prime game."""

from brain_games import cli
from brain_games.games import drive


def main():
    """Run the game."""
    print('\nWelcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no"\n')
    user_name = cli.welcome_user()
    drive.cycle(user_name, 'prime')


if __name__ == '__main__':
    main()
