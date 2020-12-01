#!/usr/bin/env python3

from collections import defaultdict
import itertools as it


dirmap = {'<': (-1, 0), '>': (1, 0), '^': (0, 1), 'v': (0, -1)}


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def main():
    input = open('input').read().strip()
    input = [dirmap[c] for c in input.lower()]

    pos = (0, 0)
    map = defaultdict(int, {pos: 1})
    for dir in input:
        pos = cadd(pos, dir)
        map[pos] += 1
    s1 = len(map)

    pos = [(0, 0)] * 2
    map = defaultdict(int, {pos[0]: 1})
    for i, dir in enumerate(input):
        im = i % 2
        pos[im] = cadd(pos[im], dir)
        map[pos[im]] += 1
    s2 = len(map)

    print(s1)
    print(s2)


main()
