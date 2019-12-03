#!/usr/bin/env python3

import itertools as it
from collections import defaultdict


dimap = {'D': (0, 1), 'U': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def add(xs, ys):
    s = tuple(x + y for x, y in zip(xs, ys))
    return s

def mdist(xs):
    return sum(abs(x) for x in xs)


input = open('input').read().strip()
paths = [[(dimap[d[0]], int(d[1:])) for d in l.split(',')] for l in input.split('\n')]

table = defaultdict(dict)
for k, path in enumerate(paths):
    cpos = (0, 0)
    s = 0
    for d, l in path:
        for _ in range(l):
            s += 1
            cpos = add(cpos, d)
            r = table[cpos]
            if k not in r:
                r[k] = s

s1 = min(mdist(xs) for xs, ps in table.items() if len(ps) == len(paths) and xs != (0, 0))
s2 = min(sum(ps.values()) for xs, ps in table.items() if len(ps) == len(paths) and xs != (0, 0))

print(s1)
print(s2)
