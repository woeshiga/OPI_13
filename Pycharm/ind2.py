#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def cats(**kwargs):
    if kwargs:
        for name, age in kwargs.items():
            if name == 'Кнопа':
                print(f'Самая милая кошка: {name}, ей уже {age}', file=sys.stderr)
            else:
                print(f'{name} радует мир своим существованием уже {age}!!!')

    else:
        return None


if __name__ == '__main__':
    cats(Вася=1, Протон=2, Борис=4, Кнопа=2)
