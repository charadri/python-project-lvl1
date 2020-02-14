# -*- coding:utf-8 -*-

"""Prime game."""

from brain_games import cli
from brain_games.games import drive


def main():
    """Run the game."""
    user_name = cli.welcome_user('prime')
    drive.cycle(user_name, 'prime')


if __name__ == '__main__':
    main()
