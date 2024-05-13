#!/usr/bin/env python3

import itertools as it


def accsum(l):
    for i in range(1, len(l)):
        l[i] += l[i - 1]


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = input.strip().split('\n')

    Xmax = len(input[0]) - 1
    Ymax = len(input) - 1

    galaxies = []
    empty_x = [1] * (Xmax + 1)
    empty_y = [1] * (Ymax + 1)
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            pos = (x, y)
            if c == '#':
                galaxies.append(pos)
                empty_x[x] = 0
                empty_y[y] = 0

    accsum(empty_x)
    accsum(empty_y)

    s1 = s2 = 0
    for g1, g2 in it.combinations(galaxies, 2):
        mx = min(g1[0], g2[0])
        my = min(g1[1], g2[1])
        Mx = max(g1[0], g2[0])
        My = max(g1[1], g2[1])

        pdiff = (Mx - mx) + (My - my)
        duplx = empty_x[Mx] - empty_x[mx]
        duply = empty_y[My] - empty_y[my]
        dups = duplx + duply

        s1 += pdiff + dups
        s2 += pdiff + (1000000 - 1) * dups

    print(s1)
    print(s2)


main()
