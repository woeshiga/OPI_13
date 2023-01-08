#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Сумму аргументов,
# расположенных после максимального аргумента.

def summa(*args):
    if args:
        return sum(args[args.index(max(args)) + 1:])

    else:
        return None


if __name__ == '__main__':
    print(summa(1, 2, -3, 4, 5, 4, 1))
    