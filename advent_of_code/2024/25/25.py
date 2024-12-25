#!/usr/bin/env python3


from collections import defaultdict
import itertools as it
import math


def main():
    input = open('input').read()
    # input = open('input_test').read()

    keys, locks = set(), set()
    for block in input.strip().split('\n\n'):
        bmM = defaultdict(lambda: [math.inf, 0])

        for y, l in enumerate(block.splitlines()):
            for x, c in enumerate(l):
                if c == '#':
                    bmM[x][0] = min(bmM[x][0], y)
                    bmM[x][1] = max(bmM[x][1], y)

        (locks, keys)[c == '#'].add(
            tuple(bmM[xx][1] - bmM[xx][0] + 1 for xx in range(x + 1))
        )
    M = y + 1

    s1 = sum(
        all(l + k <= M for l, k in zip(lock, key))
        for lock, key in it.product(locks, keys)
    )

    print(s1)


main()
