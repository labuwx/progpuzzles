#!/usr/bin/env python3


dirmap = {'^': (0, -1), 'V': (0, 1), '<': (-1, 0), '>': (1, 0)}


def tadd(a, b):
    return tuple(ax + bx for ax, bx in zip(a, b))


def rot90(d):
    return (-d[1], d[0])


def run_guard(map, pos, dir):
    visited = set()
    while True:
        if (pos, dir) in visited:
            return {pos for pos, _ in visited}, True
        else:
            visited.add((pos, dir))

        npos = tadd(pos, dir)
        if npos not in map:
            break

        if map[npos] == '#':
            dir = rot90(dir)
        else:
            pos = npos

    return {pos for pos, _ in visited}, False


def main():
    input = open('input').read()
    # input = open('input_test').read()

    map = {
        (x, y): c
        for y, l in enumerate(input.strip().splitlines())
        for x, c in enumerate(l)
    }
    startpos, startdir = next((pos, dirmap[c]) for pos, c in map.items() if c in dirmap)

    visited, _ = run_guard(map, startpos, startdir)

    s1 = len(visited)
    s2 = sum(
        run_guard(map | {pos: '#'}, startpos, startdir)[1]
        for pos in visited
        if pos != startpos
    )

    print(s1)
    print(s2)


main()
