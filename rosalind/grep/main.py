#!/usr/bin/env python3

import itertools as it

from bioinf_common import *


ds = get_dataset()
S = ds.split()
k = len(S[0]) - 1

edges = [(s[:-1], s[1:]) for s in S]
sedges = sorted(edges)
edges = set(edges)
nodes = {e[t] for e, t in it.product(edges, range(2))}

e0 = (S[0][:-1], S[0][1:])
q = [(e0, [])]
cycles = []
while q:
    e1, p = q.pop()
    if len(p) < len(S):
        nes = [e2 for e2 in edges if e1[1] == e2[0]]
        for e2 in nes:
            q.append((e2, p + [e1]))
    elif e0 == e1 and sedges == sorted(p):
        cycles.append(p)

res = [e0[0] + ''.join(e[1][-1] for e in c[:-k]) for c in cycles]

for s in res:
    print(s)
