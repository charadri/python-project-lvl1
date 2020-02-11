# -*- coding:utf-8 -*-

"""Main script."""

from brain_games import cli, even


def main():
    """Run the game."""
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    user_name = cli.welcome_user()
    even.game(user_name)


if __name__ == '__main__':
    main()
