#!/usr/bin/env python3

from collections import defaultdict, Counter


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


dirs = {
    'ne': (1, 0),
    'se': (0, 1),
    'e': (1, 1),
    'sw': (-1, 0),
    'nw': (0, -1),
    'w': (-1, -1),
}


def sum_path(path):
    pos = (0, 0, 0)
    for d in path:
        pos = cadd(pos, d)
    return pos


def parse_dir(l):
    curr_dir = ''
    path = []
    for c in l:
        curr_dir += c
        if curr_dir in dirs:
            path.append(dirs[curr_dir])
            curr_dir = ''
    assert curr_dir == ''
    return path


def main():
    input = open('input').read().split()
    # input = open('input_test').read().split()
    paths = [parse_dir(l) for l in input]

    tiles1 = defaultdict(int)
    for path in paths:
        tile = sum_path(path)
        tiles1[tile] = (tiles1[tile] + 1) % 2
    s1 = sum(tiles1.values())

    tiles2 = {pos for pos, v in tiles1.items() if v == 1}
    for _ in range(100):
        adj_cnt = Counter({tile: 0 for tile in tiles2})
        for tile in tiles2:
            for d in dirs.values():
                next_tile = cadd(tile, d)
                adj_cnt[next_tile] += 1
        tiles2 = {
            tile
            for tile, k in adj_cnt.items()
            if (tile in tiles2 and 1 <= k <= 2) or (tile not in tiles2 and k == 2)
        }
    s2 = len(tiles2)

    print(s1)
    print(s2)


main()
