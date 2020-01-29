# -*- coding:utf-8 -*-

"""CLI interaction."""

import prompt


def welcome_user():
    """Greeting User."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
