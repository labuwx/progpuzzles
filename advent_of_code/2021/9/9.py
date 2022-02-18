#!/usr/bin/env python3


# assumptions:
#  - each <9 point is part of exactly one basin


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def neighbours(map, p):
    return (q for d in dirs if (q := cadd(p, d)) in map)


def parse_map(ms):
    map = {}
    for y, l in enumerate(ms.split('\n')):
        for x, v in enumerate(l):
            map[(x, y)] = int(v)

    return map


def basin_size(map, p0):
    q, seen = [p0], set()
    while q:
        p = q.pop()
        if p in seen:
            continue
        seen.add(p)
        q.extend(p2 for p2 in neighbours(map, p) if map[p2] < 9)

    return len(seen)


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()

    map = parse_map(input)

    lows = [p for p, x in map.items() if all(x < map[p2] for p2 in neighbours(map, p))]
    s1 = sum(1 + map[p] for p in lows)

    basins = sorted(basin_size(map, low) for low in lows)
    s2 = basins[-3] * basins[-2] * basins[-1]

    print(s1)
    print(s2)


main()
