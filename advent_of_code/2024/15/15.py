#!/usr/bin/env python3


directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = input.strip().split('\n\n')

    map = {}
    for y, l in enumerate(input[0].strip().splitlines()):
        for x, c in enumerate(l):
            pos = (x, y)
            if c != '#':
                map[pos] = c
            if c == '@':
                S = pos
                map[pos] = '.'

    steps = [directions[s] for s in input[1] if s != '\n']

    pos = S
    for step in steps:
        npos = tadd(pos, step)
        if npos not in map:
            continue

        nnpos = npos
        while nnpos in map:
            if map[nnpos] == '.':
                map[npos], map[nnpos] = map[nnpos], map[npos]
                break
            nnpos = tadd(nnpos, step)

        if map[npos] == '.':
            pos = npos
            continue

    s1 = sum(x + 100 * y for (x, y), c in map.items() if c == 'O')

    print(s1)


main()
