#!/usr/bin/env python3

import re


smap = {
    'n': (0, 2),
    's': (0, -2),
    'ne': (1, 1),
    'se': (1, -1),
    'nw': (-1, 1),
    'sw': (-1, -1),
}


def dist(h, v):
    h, v = abs(h), abs(v)
    diags = min(h, v)
    h -= diags
    v -= diags
    v /= 2
    ndiags = h + v
    return diags + ndiags


input = re.sub(r'\s', '', open('input').read()).split(',')

h = v = 0
dmax = 0
for s in input:
    h += smap[s][0]
    v += smap[s][1]
    dmax = max(dmax, dist(h, v))

alls = dist(h, v)

print(alls)
print(dmax)
