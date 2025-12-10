#!/usr/bin/env python3


import itertools as it


def area(x1, y1, x2, y2):
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def main():
    input = open('input').read()
    # input = open('input_test').read()

    input = [tuple(int(x) for x in l.split(',')) for l in input.strip().splitlines()]

    s1 = max(area(x1, y1, x2, y2) for (x1, y1), (x2, y2) in it.combinations(input, 2))

    print(s1)


main()
