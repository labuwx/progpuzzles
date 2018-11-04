#!/usr/bin/env python3

from bioinf_common import *


def sc(edges):
    v0 = edges[0][0]
    dist = {edges[0][1]: edges[0][2]}
    while True:
        cross_edges = {e for e in edges if e[0] in dist.keys() and e[1] not in dist.keys()}
        if not cross_edges: break
        e = min(cross_edges, key=lambda e: e[2] + dist[e[0]])
        dist[e[1]] = dist[e[0]] + e[2]
        if e[1] == v0:
            return dist[v0]
    return -1


ds = get_dataset()
graphs = from_edgelist(ds)

issq = [sc(edges) for _, edges in graphs]
print(*issq)
