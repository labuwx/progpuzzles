#!/usr/bin/env python3

import itertools as it
import numpy as np


navmap = {'E': (1, 0), 'W': (-1, 0), 'N': (0, 1), 'S': (0, -1)}


def rotate(heading, w, angle):  # left
    for _ in range(angle // 90):
        r = 1 if w == 'R' else -1
        heading = (r * heading[1], -r * heading[0])
    return heading


def cadd(a, b, c=1):
    return tuple(ai + c * bi for ai, bi in zip(a, b))


def navigate(directions, heading, use_waypoint):
    pos = (0, 0)
    for d, n in directions:
        if d in navmap:
            if use_waypoint:
                heading = cadd(heading, navmap[d], n)
            else:
                pos = cadd(pos, navmap[d], n)
        elif d == 'F':
            pos = cadd(pos, heading, n)
        else:
            heading = rotate(heading, d, n)
    return pos


def manhattan(pos):
    return sum(abs(x) for x in pos)


def main():
    input = [(l[0], int(l[1:])) for l in open('input').read().split()]

    pos1 = navigate(input, navmap['E'], use_waypoint=False)
    s1 = manhattan(pos1)

    heading2 = cadd(navmap['N'], navmap['E'], 10)
    pos2 = navigate(input, heading2, use_waypoint=True)
    s2 = manhattan(pos2)

    print(s1)
    print(s2)


main()
