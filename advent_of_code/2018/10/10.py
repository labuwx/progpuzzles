#!/usr/bin/env python3

import itertools as it
import numpy as np
import re
from collections import deque
from matplotlib import pyplot as plt


def display(pos):
    pixels = list(set(pos.values()))
    X = np.array([p[0] for p in pixels])
    Y = np.array([-p[1] for p in pixels])
    plt.scatter(X, Y)
    plt.show()


def move(data, pos, itn):
    for i, (_, v) in enumerate(data):
        pos[i] = (pos[i][0] + v[0] * itn, pos[i][1] + v[1] * itn)


input = open('input').read().strip().split('\n')
rx = re.compile(r'^position=<\s*(?P<px>-?\d+),\s*(?P<py>-?\d+)> velocity=<\s*(?P<vx>-?\d+),\s*(?P<vy>-?\d+)>$')
data = [((int(m.group('px')), int(m.group('py'))), (int(m.group('vx')), int(m.group('vy')))) for m in (rx.match(l) for l in input)]

pos = {i: p for i, (p, _) in enumerate(data)}

for i in it.count():
    Ys = {c[1] for c in pos.values()}
    ymin, ymax = min(Ys), max(Ys)
    height = ymax - ymin
    if len(Ys) == height + 1 and height <= 10:
        break
    move(data, pos, 1)

print(i)
display(pos)
