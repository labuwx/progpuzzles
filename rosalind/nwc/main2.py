#!/usr/bin/env python3

import math

from bioinf_common import *


ds = get_dataset()
graphs = from_edgelist(ds)

# nwc = [
    # 1 if any(bellman_ford(nodes, edges, start) == None for start in nodes) else -1
    # for nodes, edges in graphs
# ]

nwc = []
for nodes, edges in graphs[len(graphs)//4:len(graphs)//4*2]:
    snodes, nc = set(nodes), False
    while snodes:
        start = next(iter(snodes))
        dist = bellman_ford(nodes, edges, start)
        if dist == None:
            nc = True
            break
        snodes -= {u for u, d in dist.items() if d < math.inf}
    nwc.append(1 if nc else -1)

print(*nwc)
