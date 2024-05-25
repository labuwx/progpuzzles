#!/usr/bin/env python3

import itertools as it
import numpy as np


def calc_1(map):
    yM, xM = len(map) - 1, len(map[0]) - 1
    s = 0
    for x in range(xM + 1):
        last_free = 0
        for y in range(yM + 1):
            match map[y][x]:
                case 'O':
                    s += yM - last_free + 1
                    last_free += 1
                case '#':
                    last_free = y + 1
    return s


def calc_2(map):
    yM = map.shape[0] - 1
    s = sum(yM - y + 1 for (y, _), c in np.ndenumerate(map) if c == 'O')
    return s


def tilt_north(map):
    yM, xM = len(map) - 1, len(map[0]) - 1
    for x in range(xM + 1):
        last_free = 0
        for y in range(yM + 1):
            match map[y][x]:
                case 'O':
                    if last_free != y:
                        map[last_free][x] = 'O'
                        map[y][x] = '.'
                    last_free += 1
                case '#':
                    last_free = y + 1


def main():
    niter = 1000000000
    input = open('input').read()
    # input = open('input_test').read()
    map1 = np.array([list(l) for l in input.strip().splitlines()])

    s1 = calc_1(map1)

    map2 = map1.copy()
    maps = [map2.copy()]
    for k in it.count(1):
        for _ in range(4):
            tilt_north(map2)
            map2 = np.rot90(map2, k=-1)
        if (
            j := next((j for j, m in enumerate(maps) if (m == map2).all()), None)
        ) is not None:
            # found the first recurrence
            break
        else:
            maps.append(map2.copy())

    # head offset + offset within the cycle
    m_idx = j + (niter - j) % (k - j)
    map2 = maps[m_idx]
    s2 = calc_2(map2)

    print(s1)
    print(s2)


main()
