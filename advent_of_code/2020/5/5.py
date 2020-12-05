#!/usr/bin/env python3

import itertools as it


def parse_pos(raw_pos):
    pos = (
        raw_pos.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    )
    pos = (int(pos[:7], 2), int(pos[7:], 2))
    return pos


def seat_id(pos):
    id = pos[0] * 8 + pos[1]
    return id


def main():
    input = open('input').read().split()
    poses = [parse_pos(p) for p in input]
    ids = sorted(seat_id(p) for p in poses)

    s1 = ids[-1]
    s2 = next(
        id1 + 1 for id1, id2 in zip(ids, it.islice(ids, 1, None)) if id2 == id1 + 2
    )

    print(s1)
    print(s2)


main()
