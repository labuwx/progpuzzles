#!/usr/bin/env python3

from collections import defaultdict, deque

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)
directions = [UP, DOWN, LEFT, RIGHT]


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def get_nbrs(regions, pos):
    return [
        nbr
        for dir in directions
        if (nbr := tadd(pos, dir)) in regions and regions[pos] == regions[nbr]
    ]


def main():
    input = open('input').read()
    # input = open('input_test').read()

    map = {
        (x, y): c
        for y, l in enumerate(input.strip().splitlines())
        for x, c in enumerate(l)
    }

    regions = {}
    q = deque([(pos, pos) for pos in map.keys()])
    while q:
        pos, reg = q.pop()
        if pos in regions:
            continue
        regions[pos] = reg

        q.extend((nbr, reg) for nbr in get_nbrs(map, pos))

    area, perim, fenc = defaultdict(int), defaultdict(int), defaultdict(int)
    for pos, reg in regions.items():
        (x, y) = pos
        area[reg] += 1
        perim[reg] += 4 - len(get_nbrs(regions, pos))

        for dir in [LEFT, RIGHT]:
            nbr_side = tadd(pos, dir)
            nbr_up = tadd(pos, UP)
            nbr_sideup = tadd(nbr_side, UP)
            fenc[reg] += reg != regions.get(nbr_side) and (
                regions.get(nbr_up) != reg or regions.get(nbr_sideup) == reg
            )

        for dir in [UP, DOWN]:
            nbr_side = tadd(pos, dir)
            nbr_left = tadd(pos, LEFT)
            nbr_sideleft = tadd(nbr_side, LEFT)
            fenc[reg] += reg != regions.get(nbr_side) and (
                regions.get(nbr_left) != reg or regions.get(nbr_sideleft) == reg
            )

    s1 = sum(ar * perim[reg] for reg, ar in area.items())
    s2 = sum(ar * fenc[reg] for reg, ar in area.items())

    print(s1)
    print(s2)


main()
