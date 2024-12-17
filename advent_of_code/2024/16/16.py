#!/usr/bin/env python3

from heapq import heapify, heappush, heappop


NORTH, SOUTH, WEST, EAST = (0, -1), (0, 1), (-1, 0), (1, 0)
directions = [NORTH, SOUTH, WEST, EAST]


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def inv(x):
    return tuple(-xx for xx in x)


def rot90(d, rev=False):
    t = -1 if rev else 1
    return (-t * d[1], t * d[0])


def dijkstra(map, q):
    q = list(q)
    heapify(q)

    reached = {}
    while q:
        score, pos, dir = heappop(q)

        if pos not in map or (key := (pos, dir)) in reached:
            continue
        else:
            reached[key] = score

        heappush(q, (score + 1, tadd(pos, dir), dir))
        heappush(q, (score + 1000, pos, rot90(dir, rev=False)))
        heappush(q, (score + 1000, pos, rot90(dir, rev=True)))

    return reached


def main():
    input = open('input').read()
    # input = open('input_test').read()

    map = set()
    for y, l in enumerate(input.strip().splitlines()):
        for x, c in enumerate(l):
            pos = (x, y)
            if c != '#':
                map.add(pos)
            if c == 'S':
                S = pos
            elif c == 'E':
                E = pos

    r1 = dijkstra(map, [(0, S, EAST)])
    r2 = dijkstra(map, [(0, E, dir) for dir in directions])

    s1 = min(r1[(E, dir)] for dir in directions)
    s2 = sum(
        any(s1 == r1[(pos, dir)] + r2[(pos, inv(dir))] for dir in directions)
        for pos in map
    )

    print(s1)
    print(s2)


main()
