#!/usr/bin/env python3

from collections import deque, defaultdict

from bioinf_common import *


def dijkstra(edges, start):
    dist = defaultdict(lambda: -1, {start: 0})
    while True:
        cross_edges = {
            e for e in edges if e[0] in dist.keys() and e[1] not in dist.keys()
        }
        if not cross_edges:
            break
        e = min(cross_edges, key=lambda e: e[2] + dist[e[0]])
        dist[e[1]] = dist[e[0]] + e[2]
    return dist


ds = get_dataset()
nodes, edges = from_edgelist(ds)

dist = dijkstra(edges, 1)
dist_v = [dist[u] for u in nodes]

print(*dist_v)
