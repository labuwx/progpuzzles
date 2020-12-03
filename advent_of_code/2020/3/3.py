#!/usr/bin/env python3


def tree_encounter(map, slope):
    height, width = len(map), len(map[0])
    sx, sy = slope

    ntree, x, y = 0, 0, 0
    while y < height:
        ntree += map[y][x]
        y += sy
        x = (x + sx) % width

    return ntree


def main():
    input = open('input').read().strip().split('\n')
    map = [[1 if c == '#' else 0 for c in l] for l in input]
    main_slope = (3, 1)
    test_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    s1 = tree_encounter(map, main_slope)

    s2 = 1
    for slope in test_slopes:
        s2 *= tree_encounter(map, slope)

    print(s1)
    print(s2)


main()
