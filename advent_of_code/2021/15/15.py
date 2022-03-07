#!/usr/bin/env python3

from heapq import heappush, heappop
import itertools as it


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def neighbours(map, p):
    return (q for d in dirs if (q := cadd(p, d)) in map)


def parse_input(input):
    map = {
        (x, y): int(c) for y, l in enumerate(input.split('\n')) for x, c in enumerate(l)
    }
    xm = max(x for x, _ in map)

    return map, (xm, xm)


def tilemap(map):
    scale = 5
    n = max(x for x, _ in map) + 1
    nmap = {
        (x, y): (map[(x % n, y % n)] + x // n + y // n - 1) % 9 + 1
        for x, y in it.product(range(scale * n), repeat=2)
    }
    return nmap, (scale * n - 1, scale * n - 1)


def traverse(map, endpos):
    reached, heap_cnt = set(), it.count()
    q = [(0, next(heap_cnt), (0, 0))]
    while q:
        risk, _, pos = heappop(q)

        if pos in reached:
            continue
        else:
            reached.add(pos)

        if pos == endpos:
            return risk

        for npos in neighbours(map, pos):
            if npos in reached:
                continue
            nrisk = risk + map[npos]
            heappush(q, (nrisk, next(heap_cnt), npos))


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()

    map1, endpos1 = parse_input(input)
    map2, endpos2 = tilemap(map1)

    s1 = traverse(map1, endpos1)
    s2 = traverse(map2, endpos2)

    print(s1)
    print(s2)


main()
