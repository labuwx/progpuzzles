#!/usr/bin/env python3


from collections import defaultdict
import itertools as it


def tadd(a, b, t=1):
    return tuple(ax + t * bx for ax, bx in zip(a, b))


def parse_input(txt):
    antennas = defaultdict(list)
    for y, l in enumerate(txt.strip().splitlines()):
        for x, c in enumerate(l):
            if c != '.':
                antennas[c].append((x, y))
    xM, yM = x, y

    return dict(antennas), (xM, yM)


def find_antinodes_1(antennas, inmap):
    antinodes = set()
    for f_ants in antennas.values():
        for a1, a2 in it.combinations(f_ants, 2):
            d = tadd(a2, a1, -1)
            antinodes.add(tadd(a2, d))
            antinodes.add(tadd(a1, d, -1))

            if d[0] % 3 == 0 == d[1] % 3:
                d3 = (d[0] // 3, d[1] // 3)
                antinodes.add(tadd(a1, d3))
                antinodes.add(tadd(a1, d3, 2))

    return [an for an in antinodes if inmap(an)]


def find_antinodes_2(antennas, inmap):
    antinodes = set()
    for f_ants in antennas.values():
        for a1, a2 in it.combinations(f_ants, 2):
            d = tadd(a2, a1, -1)

            an = a1
            while inmap(an := tadd(an, d)):
                antinodes.add(an)

            an = a2
            while inmap(an := tadd(an, d, -1)):
                antinodes.add(an)

    return list(antinodes)


def main():
    input = open('input').read()
    # input = open('input_test').read()

    antennas, M = parse_input(input)
    inmap = lambda pos: 0 <= pos[0] <= M[0] and 0 <= pos[1] <= M[1]

    s1 = len(find_antinodes_1(antennas, inmap))
    s2 = len(find_antinodes_2(antennas, inmap))

    print(s1)
    print(s2)


main()
