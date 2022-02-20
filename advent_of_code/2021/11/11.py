#!/usr/bin/env python3

from collections import deque
import itertools as it

dirs = [d for d in it.product([-1, 0, 1], repeat=2) if d != (0, 0)]


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def neighbours(map, p):
    return (q for d in dirs if (q := cadd(p, d)) in map)


def parse_input(input):
    map = {}
    for y, l in enumerate(input.split('\n')):
        for x, v in enumerate(l.strip()):
            map[(x, y)] = int(v)

    return map


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()
    map = parse_input(input)
    n_steps = 100

    i, s1, s2 = 0, 0, None
    while True:
        i += 1
        next_flash = deque()
        for p in map:
            map[p] += 1
            if map[p] > 9:
                next_flash.append(p)

        step_flash = 0
        while next_flash:
            step_flash += 1
            p = next_flash.pop()
            for q in neighbours(map, p):
                v = map[q]
                if v > 9:
                    continue
                if v == 9:
                    next_flash.append(q)
                map[q] += 1

        for p in map:
            map[p] %= 10

        s1 += step_flash if i <= n_steps else 0
        if s2 is None and step_flash == len(map):
            s2 = i

        if s2 is not None and i >= n_steps:
            break

    print(s1)
    print(s2)


main()
