#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
strings = ds.split()

nodes, edges = {'': 1}, []
k = 1
for s in strings:
    p = ''
    for c in s:
        p += c
        if nodes.get(p, None) is None:
            k += 1
            nodes[p] = k
            e = ((nodes[p[:-1]], k), c)
            edges.append(e)

for (u, v), c in edges:
    print(u, v, c)
