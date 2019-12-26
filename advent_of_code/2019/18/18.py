#!/usr/bin/env python3

import itertools as it
import re
from collections import deque


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def add(a, b, n=1):
    return tuple(ai + n * bi for ai, bi in zip(a, b))


def parse_map(mapstr):
    map = {}
    tunnel = re.compile(r'[.@a-zA-Z]')
    for pos, c in mapstr.items():
        if not tunnel.match(c):
            continue
        if c == '@':
            start_pos = pos

        map[pos] = (
            c.lower() if 'A' <= c <= 'Z' else None,
            c if 'a' <= c <= 'z' else None,
        )

    return map, start_pos


def transform_map(map, start_pos):
    map = dict(map)

    map.pop(start_pos, None)
    for dir in directions:
        map.pop(add(start_pos, dir), None)

    new_start_poss = [add(start_pos, dir) for dir in it.product([-1, 1], repeat=2)]
    return map, new_start_poss


def replace(l, k, y):
    return tuple(x if i != k else y for i, x in enumerate(l))


def bfs(map, start_poss):
    nkeys = len({key for _, key in map.values() if key != None}) + 1
    q = deque(
        [
            (
                tuple(start_poss),
                frozenset({map[pos][1] for pos in start_poss} | {None}),
                0,
            )
        ]
    )
    reached = [set() for _ in range(len(start_poss))]
    while q:
        poss, keys, steps = q.popleft()

        if nkeys == len(keys):
            return steps

        for i, pos in enumerate(poss):
            if (reach_entry := (pos, keys)) in reached[i]:
                continue
            else:
                reached[i].add(reach_entry)

            for nb in (add(pos, dir) for dir in directions):
                if nb in map and map[nb][0] in keys:
                    new_keys = frozenset(keys | {map[nb][1]})
                    q.append((replace(poss, i, nb), new_keys, steps + 1))


def main():
    input = {
        (x, y): c
        for y, l in enumerate(open('input').read().split('\n'))
        for x, c in enumerate(l)
    }
    map, start_pos = parse_map(input)
    s1 = bfs(map, [start_pos])

    map2, start_poss2 = transform_map(map, start_pos)
    s2 = bfs(map2, start_poss2)

    print(s1)
    print(s2)


main()
