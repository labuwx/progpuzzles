#!/usr/bin/env python3

import itertools as it
import re


def display(pos):
    pos = set(pos)
    filler = '#'
    xmin, xmax = min(p[0] for p in pos), max(p[0] for p in pos)
    ymin, ymax = min(p[1] for p in pos), max(p[1] for p in pos)
    for y in range(ymin, ymax + 1):
        l = ''.join(filler if (x, y) in pos else ' ' for x in range(xmin, xmax + 1))
        print(l)


def move(data, pos, itn=1):
    for i, (_, v) in enumerate(data):
        pos[i] = (pos[i][0] + v[0] * itn, pos[i][1] + v[1] * itn)


input = open('input').read().strip().split('\n')
rx = re.compile(
    r'^position=<\s*(?P<px>-?\d+),\s*(?P<py>-?\d+)> velocity=<\s*(?P<vx>-?\d+),\s*(?P<vy>-?\d+)>$'
)
data = [
    ((int(m.group('px')), int(m.group('py'))), (int(m.group('vx')), int(m.group('vy'))))
    for m in (rx.match(l) for l in input)
]

pos = {i: p for i, (p, _) in enumerate(data)}

for i in it.count():
    Ys = {c[1] for c in pos.values()}
    ymin, ymax = min(Ys), max(Ys)
    height = ymax - ymin + 1
    if height == 10:
        break
    move(data, pos)

display(pos.values())
print(i)
