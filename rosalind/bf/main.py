#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
nodes, edges = from_edgelist(ds)
dist = bellman_ford(nodes, edges, 1)
dist = [dist[u] if dist[u] < math.inf else 'x' for u in sorted(nodes)]

print(*dist)
