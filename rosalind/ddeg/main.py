#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
nodes, edges = from_edgelist(ds)
edges = [set(e) for e in edges]

deg = {u: sum(1 for e in edges if u in e) for u in nodes}
ddeg = {u: sum(deg[v] for v in nodes if {u, v} in edges) for u in nodes}

print(*(ddeg[u] for u in nodes))
