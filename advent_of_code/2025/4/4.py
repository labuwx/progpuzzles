#!/usr/bin/env python3

import itertools as it
from collections import deque


def nbrs(pos):
    x, y = pos
    dd = [-1, 0, 1]
    return {
        (x + xd, y + yd) for xd, yd in it.product(dd, repeat=2) if (xd, yd) != (0, 0)
    }


def main():
    input = open('input').read()
    # input = open('input_test').read()

    input = {
        (x, y)
        for y, l in enumerate(input.strip().splitlines())
        for x, c in enumerate(l)
        if c == '@'
    }

    rolls = {pos: len(nbrs(pos) & input) for pos in input}
    q = deque([pos for pos, cnt_nbrs in rolls.items() if cnt_nbrs < 4])
    s1 = len(q)

    removed = set()
    while q:
        r = q.pop()
        if r in removed:
            continue

        removed.add(r)

        for nb in nbrs(r) & rolls.keys():
            rolls[nb] -= 1
            if rolls[nb] < 4:
                q.append(nb)

    s2 = len(removed)

    print(s1)
    print(s2)


main()
