#!/usr/bin/env python3


from collections import deque


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def tadd(a, b, t=1):
    return tuple(ax + t * bx for ax, bx in zip(a, b))


def rot90(d, rev=False):
    t = -1 if rev else 1
    return (-t * d[1], t * d[0])


def ndir(d, c):
    match d, c:
        case ((0, -1), '-') | ((0, 1), '-'):
            return [(-1, 0), (1, 0)]
        case ((-1, 0), '|') | ((1, 0), '|'):
            return [(0, -1), (0, 1)]
        case ((1, 0), '\\') | ((0, 1), '/') | ((-1, 0), '\\') | ((0, -1), '/'):
            return [rot90(d, rev=False)]
        case ((1, 0), '/') | ((0, 1), '\\') | ((-1, 0), '/') | ((0, -1), '\\'):
            return [rot90(d, rev=True)]
        case _:
            return [d]


def count_energized(map, init):
    q = deque([init])
    visited = set()
    energized_tile = set()
    while q:
        p, d = (pd := q.popleft())
        if pd in visited:
            continue
        visited.add(pd)
        energized_tile.add(p)
        for nd in ndir(d, map[p]):
            np = tadd(p, nd)
            if np not in map:
                continue
            q.append((np, nd))

    return len(energized_tile)


def main():
    input = open('input').read()
    # input = open('input_test').read()

    map = {
        (x, y): c
        for y, l in enumerate(input.strip().splitlines())
        for x, c in enumerate(l)
    }

    s1 = count_energized(map, ((0, 0), (1, 0)))

    s2 = max(
        count_energized(map, (p, d))
        for p in map.keys()
        for d in directions
        if tadd(p, d, -1) not in map
    )

    print(s1)
    print(s2)


main()
