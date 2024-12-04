#!/usr/bin/env python3

import itertools as it


directions = [p for p in it.product([-1, 0, 1], repeat=2) if p != (0, 0)]


def tadd(a, b, t=1):
    return tuple(ax + t * bx for ax, bx in zip(a, b))


def match1(map, offset):
    tf = lambda dir, k: map.get(tadd(offset, dir, k))
    return sum(all(tf(dir, k) == c for k, c in enumerate('XMAS')) for dir in directions)


def match2(map, offset):
    tf = lambda x, y: map.get(tadd(offset, (x, y)))
    return tf(1, 1) == 'A' and {tf(0, 0), tf(2, 2)} == set('MS') == {tf(0, 2), tf(2, 0)}


def main():
    input = open('input').read()
    # input = open('input_test').read()

    map = {
        (x, y): c
        for y, l in enumerate(input.strip().splitlines())
        for x, c in enumerate(l)
    }

    s1 = sum(match1(map, offset) for offset in map)
    s2 = sum(match2(map, offset) for offset in map)

    print(s1)
    print(s2)


main()
