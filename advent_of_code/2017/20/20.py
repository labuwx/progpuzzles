#!/usr/bin/env python3

import numpy as np
import re
from collections import Counter

def manhattan(p):
    return np.abs(p).sum()

input = open('input').read()

points = []
for line in input.split('\n'):
    if line == '': continue
    m = re.match(r'p=<(?P<p1>-?\d+),(?P<p2>-?\d+),(?P<p3>-?\d+)>, v=<(?P<v1>-?\d+),(?P<v2>-?\d+),(?P<v3>-?\d+)>, a=<(?P<a1>-?\d+),(?P<a2>-?\d+),(?P<a3>-?\d+)>', line)
    p1, p2, p3, v1, v2, v3, a1, a2, a3 = map(lambda name: float(m.group(name)), ['p1', 'p2', 'p3', 'v1', 'v2', 'v3', 'a1', 'a2', 'a3'])
    points.append({
        'p': np.array([p1, p2, p3]),
        'v': np.array([v1, v2, v3]),
        'a': np.array([a1, a2, a3])
    })

idxs2del = set()
for _ in range(100):
    positions = Counter(tuple(p['p']) for p in points)
    for i, p in enumerate(points):
        pv = tuple(p['p'])
        if positions[pv] > 1:
            idxs2del.add(i)
        p['v'] += p['a']
        p['p'] += p['v']

imin, dmin = 0, manhattan(points[0]['p'])
for i, p in enumerate(points):
    dst = manhattan(p['p'])
    if dst < dmin:
        imin = i
        dmin = dst

pleft = len(points) - len(idxs2del)


print(imin)
print(pleft)
