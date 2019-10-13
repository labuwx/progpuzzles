#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
graphs = from_edgelist(ds)

sc = []
for nodes, edges in graphs:
    rev_edges = [(v, u) for u, v in edges]
    topo_order = topo_sort_dfs(nodes, edges)
    parent, reached = dfs(topo_order, rev_edges)[:2]
    reached = sorted(reached.keys(), key=reached.get)
    cnt = it.count()
    comp_map = {c: next(cnt) for c, p in parent.items() if p == None}
    for u in reached:
        if u not in comp_map.keys():
            comp_map[u] = comp_map[parent[u]]
    new_nodes = list(comp_map.values())
    # new_edges = {(comp_map[u], comp_map[v]) for u, v in rev_edges}
    new_edges = {(comp_map[u], comp_map[v]) for u, v in edges}
    new_topo_order = topo_sort_dfs(new_nodes, new_edges)
    is_sc = all((u, v) in new_edges for u, v in zip(new_topo_order, new_topo_order[1:]))
    sc.append(1 if is_sc else -1)

print(*sc)
