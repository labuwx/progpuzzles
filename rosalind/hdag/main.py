#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
graphs = from_edgelist(ds)

for nodes, edges in graphs:
    topo_order = topo_sort_dfs(nodes, edges)
    hamil = all(e in edges for e in zip(topo_order, topo_order[1:]))
    if hamil:
        print(1, *topo_order)
    else:
        print(-1)
