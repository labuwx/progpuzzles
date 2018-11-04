#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
nodes, edges = from_edgelist(ds)
rev_edges = [(v, u) for u, v in edges]

left = topo_sort_dfs(nodes, edges)
parent = dfs(left, rev_edges)[0]

num_comp = sum(1 for p in parent.values() if p == None)

print(num_comp)
