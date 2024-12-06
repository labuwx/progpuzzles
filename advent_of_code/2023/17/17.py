#!/usr/bin/env python3

from heapq import heapify, heappush, heappop
import math


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def inv(xs):
    return tuple(-x for x in xs)


def solve(map, startp, target, minsteps, maxsteps):
    q = [(-map[startp], startp, 0, (0, 1)), (-map[startp], startp, 0, (1, 0))]
    heapify(q)
    reached = {}
    while q:
        d, pos, steps, dir = heappop(q)
        nd = d + map[pos]

        if (pos, steps, dir) in reached:
            continue
        else:
            reached[(pos, steps, dir)] = nd

        for ndir in directions:
            npos = tadd(pos, ndir)
            if npos not in map or ndir == inv(dir):
                continue

            if dir != ndir and minsteps <= steps:
                heappush(q, (nd, npos, 1, ndir))
            if dir == ndir and steps < maxsteps:
                heappush(q, (nd, npos, steps + 1, ndir))

    return min(
        reached.get((target, steps, dir), math.inf)
        for steps in range(minsteps, maxsteps + 1)
        for dir in directions
    )


def main():
    input = open('input').read()
    # input = open('input_test').read()

    map = {
        (x, y): int(c)
        for y, l in enumerate(input.strip().splitlines())
        for x, c in enumerate(l)
    }
    target = max(map.keys())
    startp = (0, 0)

    s1 = solve(map, startp, target, 0, 3)
    s2 = solve(map, startp, target, 4, 10)

    print(s1)
    print(s2)


main()
