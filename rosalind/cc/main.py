#!/usr/bin/env python3

from collections import deque

from bioinf_common import *


def num_comp(n, edges):
    visited, nc = set(), 0
    for k in range(1, n + 1):
        if k in visited:
            continue

        q = deque([k])
        nc += 1
        while q:
            u = q.pop()
            visited.add(u)
            q.extend(next(iter(e - {u})) for e in edges if (u in e) and (e - visited))
    return nc


ds = get_dataset().split('\n')
n = int(ds[0].split()[0])
edges = {frozenset(int(x) for x in l.split()) for l in ds[1:]}

nc = num_comp(n, edges)

print(nc)
