#!/usr/bin/env python3

import math
from collections import defaultdict

from bioinf_common import *


ds = get_dataset()
nodes, edges = from_edgelist(ds)

topo_order = topo_sort_dfs(nodes, edges)

start = 1
dist = defaultdict(lambda: math.inf, {start: 0})
for v in topo_order:
    if v == start: continue
    dist[v] = min((dist[u] + c for u, vv, c in edges if vv == v), default=math.inf)

print(*(dist[u] if dist[u] < math.inf else 'x' for u in nodes))
