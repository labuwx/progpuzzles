#!/usr/bin/env python3

from collections import defaultdict
import itertools as it
import re


pattern = re.compile(
    r'^(?P<cmd>turn on|toggle|turn off) (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)$'
)
cmd_map = {'turn on': '+', 'turn off': '-', 'toggle': '*'}


def main():
    input = open('input').read().strip().split('\n')

    instr = []
    for l in input:
        m = pattern.match(l)
        instr.append(
            (
                cmd_map[m.group('cmd')],
                (int(m.group('x1')), int(m.group('y1'))),
                (int(m.group('x2')), int(m.group('y2'))),
            )
        )

    grid = defaultdict(int)
    for cmd, (x1, y1), (x2, y2) in instr:
        for pixel in it.product(range(x1, x2 + 1), range(y1, y2 + 1)):
            if cmd == '+':
                grid[pixel] = 1
            elif cmd == '-':
                grid[pixel] = 0
            else:
                grid[pixel] = (grid[pixel] + 1) % 2
    s1 = sum(grid.values())

    grid = defaultdict(int)
    for cmd, (x1, y1), (x2, y2) in instr:
        for pixel in it.product(range(x1, x2 + 1), range(y1, y2 + 1)):
            if cmd == '+':
                grid[pixel] += 1
            elif cmd == '-':
                grid[pixel] = max(0, grid[pixel] - 1)
            else:
                grid[pixel] += 2
    s2 = sum(grid.values())

    print(s1)
    print(s2)


main()
