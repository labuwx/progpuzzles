#!/usr/bin/env python3

import itertools as it


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def add(a, b):
    return tuple(ai + bi for ai, bi in zip(a, b))


def inf(bug, n_adj):
    if bug:
        return int(n_adj == 1)
    else:
        return int(1 <= n_adj <= 2)


def evolve1(map):
    new_map = {
        pos: inf(bug, sum(map.get(add(pos, dir), 0) for dir in directions))
        for pos, bug in map.items()
    }
    return new_map


def tiles():
    return it.product(range(-ymy, ymy + 1), range(-xmx, xmx + 1))


def neighbours(pos, level):
    x, y = pos

    # tiles to the left
    if -xmx == x:
        yield ((-1, 0), level - 1)
    elif x != 1 or y != 0:
        yield ((x - 1, y), level)
    else:
        for ynb in range(-ymy, ymy + 1):
            yield ((xmx, ynb), level + 1)

    # tiles to the right
    if xmx == x:
        yield ((1, 0), level - 1)
    elif x != -1 or y != 0:
        yield ((x + 1, y), level)
    else:
        for ynb in range(-ymy, ymy + 1):
            yield ((-xmx, ynb), level + 1)

    # tiles above
    if -ymy == y:
        yield ((0, -1), level - 1)
    elif y != 1 or x != 0:
        yield ((x, y - 1), level)
    else:
        for xnb in range(-xmx, xmx + 1):
            yield ((xnb, ymy), level + 1)

    # tiles below
    if ymy == y:
        yield ((0, 1), level - 1)
    elif y != -1 or x != 0:
        yield ((x, y + 1), level)
    else:
        for xnb in range(-xmx, xmx + 1):
            yield ((xnb, -ymy), level + 1)


def evolve2(map):
    lmin = min(level for _, level in map.keys())
    lmax = max(level for _, level in map.keys())
    lmin, lmax = lmin - 1, lmax + 1

    new_map = {
        (pos, level): inf(
            map.get((pos, level), 0),
            sum(map.get(nb, 0) for nb in neighbours(pos, level)),
        )
        for pos, level in it.product(tiles(), range(lmin, lmax + 1))
        if pos != (0, 0)
    }
    return new_map


def to_rec_map(map):
    return {(pos, 0): bug for pos, bug in map.items() if pos != (0, 0)}


def biod_rating(map):
    score = sum(map[(x, y)] * (2 ** i) for i, (y, x) in enumerate(tiles()))
    return score


def main():
    global xmx, ymy
    map = {
        (x, y): 1 if c == '#' else 0
        for y, l in enumerate(open('input').read().split('\n'))
        for x, c in enumerate(l)
    }
    xmx, ymy = max(x for x, _ in map.keys()) // 2, max(y for _, y in map.keys()) // 2
    map = {(x - xmx, y - ymy): bug for (x, y), bug in map.items()}

    ratings, map1 = set(), map
    while (s1 := biod_rating(map1)) not in ratings:
        ratings.add(s1)
        map1 = evolve1(map1)

    map2 = to_rec_map(map)
    for _ in range(200):
        map2 = evolve2(map2)
    s2 = sum(map2.values())

    print(s1)
    print(s2)


main()
