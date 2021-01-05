#!/usr/bin/env python3

from collections import defaultdict
import enum
import itertools as it
import re


CellType = enum.Enum('CellType', 'empty wall water_rest water_flow')

pattern = re.compile(
    r'(?P<dir>[xy])=(?P<c_fix>\d+), [xy]=(?P<c_min>\d+)\.\.(?P<c_max>\d+)'
)

celltype_map = {
    CellType.empty: '.',
    CellType.wall: '#',
    CellType.water_rest: '~',
    CellType.water_flow: '|',
}


def draw(map):
    xmin, xmax = min(pos[0] for pos in map), max(pos[0] for pos in map)
    ymin, ymax = min(pos[1] for pos in map), max(pos[1] for pos in map)

    for y in range(ymin, ymax + 1):
        l = [celltype_map[map[(x, y)]] for x in range(xmin, xmax + 1)]
        print(''.join(l))


def fill(map, wsrc):
    x0, y0 = wsrc
    ymax = max(pos[1] for pos, c in map.items() if c == CellType.wall)

    for y in range(y0 + 1, ymax + 1):
        if map[(x0, y)] in [CellType.wall, CellType.water_rest]:
            y_bottom = y - 1
            break
        elif map[(x0, y)] == CellType.water_flow:
            return
        else:
            map[(x0, y)] = CellType.water_flow
    else:
        return

    overflow = False
    for y in range(y_bottom, y0, -1):
        for dir in [-1, 1]:
            for x in it.count(x0, dir):
                p = (x, y)
                if map[p] == CellType.wall:
                    break
                map[p] = CellType.water_flow
                if map[(x, y + 1)] == CellType.empty:
                    fill(map, (x, y))
                if map[(x, y + 1)] == CellType.water_flow:
                    overflow = True
                    break

        if overflow:
            break

        for dir in [-1, 1]:
            for x in it.count(x0, dir):
                p = (x, y)
                if map[p] == CellType.wall:
                    break
                else:
                    map[p] = CellType.water_rest


def main():
    input = open('input').read().strip().split('\n')
    # input = open('input_test').read().strip().split('\n')
    data = [
        (m['dir'], int(m['c_fix']), (int(m['c_min']), int(m['c_max'])))
        for l in input
        for m in [pattern.fullmatch(l)]
    ]
    water0 = (500, 0)

    map = defaultdict(lambda: CellType.empty)
    for dir, cfix, (cmin, cmax) in data:
        for c in range(cmin, cmax + 1):
            pos = (cfix, c) if dir == 'x' else (c, cfix)
            map[pos] = CellType.wall
    ymin, ymax = min(pos[1] for pos in map), max(pos[1] for pos in map)

    fill(map, water0)
    # draw(map)

    nrest = sum(
        c == CellType.water_rest
        for (x, y), c in map.items()
        if ymin <= y <= ymax and (x, y) != water0
    )
    nflow = sum(
        c == CellType.water_flow
        for (x, y), c in map.items()
        if ymin <= y <= ymax and (x, y) != water0
    )
    s1 = nrest + nflow
    s2 = nrest

    print(s1)
    print(s2)


main()
