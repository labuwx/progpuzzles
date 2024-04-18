#!/usr/bin/env python3

import math


def parse_nums(s):
    return [[int(ns) for ns in l.split()] for l in s]


def parse_input(input):
    sds, *mapss = (
        parse_nums(part.split(':')[1].strip().split('\n'))
        for part in input.split('\n\n')
    )

    seeds1 = sds[0]
    seeds2 = list(zip(seeds1[::2], seeds1[1::2]))

    return seeds1, seeds2, mapss


def map_func_builder_single(map_rcp):
    def map_func(x):
        for d, s, l in map_rcp:
            if s <= x <= s + l - 1:
                return d + x - s
        return x

    return map_func


def map_func_builder(mapss):
    map_func = lambda x: x
    for maps in mapss:
        map_func = (lambda m_acc, m_curr: lambda x: m_curr(m_acc(x)))(
            map_func, map_func_builder_single(maps)
        )
    return map_func


def map_magic_builder(mapss):
    map_acc = [(0, math.inf, 0)]
    for maps in mapss:
        new_map = []
        map_cur = [(s, s + l - 1, d - s) for d, s, l in maps]

        x = 0
        for a0, a1, ad in map_acc:
            map_cur_b = sorted((b0 - ad, b1 - ad, bd) for b0, b1, bd in map_cur)

            j = 0
            while x <= a1 and x != math.inf:
                while j < len(map_cur_b) and map_cur_b[j][1] < x:
                    j += 1

                if j == len(map_cur_b):
                    c1 = a1
                    new_map.append((x, a1, ad))
                else:
                    b0, b1, bd = map_cur_b[j]
                    if x < b0:
                        c1 = min(a1, b0 - 1)
                        new_map.append((x, c1, ad))
                    else:
                        c1 = min(a1, b1)
                        new_map.append((x, c1, ad + bd))

                x = c1 + 1

        map_acc = sorted(new_map)

    return map_acc


def map_range(map, ranges):
    results = []
    for a0, l in ranges:
        a1 = a0 + l - 1
        for b0, b1, bd in map:
            c0 = max(a0, b0)
            c1 = min(a1, b1)
            if c0 <= c1:
                results.append((c0 + bd, c1 + bd))
    return results


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()

    seeds1, seeds2, mapss = parse_input(input)
    map_func = map_func_builder(mapss)
    map_magic = map_magic_builder(mapss)

    locations1_1 = [map_func(seed) for seed in seeds1]
    locations1_2 = [
        seed + next(d for a0, a1, d in map_magic if seed <= a1) for seed in seeds1
    ]
    assert locations1_1 == locations1_2
    s1 = min(locations1_1)

    s2 = min(a0 for a0, _ in map_range(map_magic, seeds2))

    print(s1)
    print(s2)


main()
