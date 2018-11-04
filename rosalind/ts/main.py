#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
nodes, edges = from_edgelist(ds)
topo_order = topo_sort_dfs(nodes, edges)

print(*topo_order)
