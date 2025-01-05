#!/usr/bin/env python3


directions = {(0, -1), (0, 1), (-1, 0), (1, 0)}


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def main():
    input, N = open('input').read(), 64
    # input, N = open('input_test').read(), 6

    map = set()
    for y, l in enumerate(input.strip().splitlines()):
        for x, c in enumerate(l):
            pos = (x, y)
            if c != '#':
                map.add(pos)
            if c == 'S':
                S = pos

    reached = {S}
    for k in range(N):
        reached = frozenset(
            npos
            for pos in reached
            for dir in directions
            if (npos := tadd(pos, dir)) in map
        )

    s1 = len(reached)
    print(s1)


main()
