#!/usr/bin/env python3

import itertools as it


# note: maybe use combinations_with_replacement()
# speedup: sort list and use binary search to find remaining element / range


def main():
    input = open('input').read()
    input = [int(x) for x in input.split()]

    for x, y in it.combinations(input, r=2):
        if x + y == 2020:
            s1 = x * y

    for x, y, z in it.combinations(input, r=3):
        if x + y + z == 2020:
            s2 = x * y * z

    print(s1)
    print(s2)


main()
