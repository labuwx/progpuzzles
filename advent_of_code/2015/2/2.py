#!/usr/bin/env python3

import itertools as it
import math


def apaper(dims):
    surface, extra = 0, math.inf

    for a, b in it.combinations(dims, r=2):
        aside = a * b
        surface += 2 * aside
        extra = min(extra, aside)

    return surface + extra


def lribbon(dims):
    perim = min(2 * sum(edges) for edges in it.combinations(dims, r=2))
    bow = dims[0] * dims[1] * dims[2]

    return perim + bow


def main():
    input = open('input').read().split()
    input = [tuple(int(x) for x in l.lower().split('x')) for l in input]

    s1 = sum(apaper(box) for box in input)
    s2 = sum(lribbon(box) for box in input)

    print(s1)
    print(s2)


main()
