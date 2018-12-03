#!/usr/bin/env python3

import itertools as it
import re
from collections import defaultdict


def fill(t, id, x, y, w, h):
    for i, j in it.product(range(x, x+w), range(y, y+h)):
        t[(i, j)].add(id)


input = open('input').read().strip().split('\n')
rx = re.compile(r'^#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)$')
entries = [tuple(int(x) for x in m.groups()) for m in (rx.match(l) for l in input)]

t = defaultdict(set)
for e in entries:
    fill(t, *e)

s1 = sum(len(b) > 1 for b in t.values())

overlap = defaultdict(lambda: False)
for v in t.values():
    for id in v:
        overlap[id] |= len(v) > 1
s2 = next(id for id, v in overlap.items() if not v)

print(s1)
print(s2)
