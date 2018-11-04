#!/usr/bin/env python3

from collections import deque, defaultdict

from bioinf_common import *


def bfs(edges, start):
    dist = defaultdict(lambda: -1, {start: 0})
    q = deque([start])
    while q:
        u = q.popleft()
        d = dist[u]
        neighbours = {e[1] for e in edges if e[0] == u and e[1] not in dist.keys()}
        q.extend(neighbours)
        dist.update({v: d+1 for v in neighbours})
    return dist


ds = get_dataset()
nodes, edges = from_edgelist(ds)

dist = bfs(edges, 1)
dist_v = [dist[u] for u in nodes]

print(*dist_v)
