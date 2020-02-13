# -*- coding:utf-8 -*-

"""Even game."""

from brain_games import cli
from brain_games.games import drive


def main():
    """Run the game."""
    user_name = cli.welcome_user('even')
    drive.cycle(user_name, 'even')


if __name__ == '__main__':
    main()
