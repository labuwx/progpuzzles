#!/usr/bin/env python3

from solvers import solve1_5 as solve1
from solvers import solve2_2 as solve2


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()
    input = [int(x) for x in input.split(',')]

    s1 = solve1(input)
    s2 = solve2(input)

    print(s1)
    print(s2)


main()
