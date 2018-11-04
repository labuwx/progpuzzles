#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
graphs = from_edgelist(ds)

gs = []
for nodes, edges in graphs:
    topo_order = topo_sort_dfs(nodes, edges)
    parent = dfs(topo_order, edges)[0]
    has_gs = sum(1 for p in parent.values() if p == None) == 1
    gs.append(topo_order[0] if has_gs else -1)

print(*gs)
