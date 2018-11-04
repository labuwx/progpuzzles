#!/usr/bin/env python3

import itertools as it

from bioinf_common import *


ds = get_dataset()
graphs = from_edgelist(ds)

for vars, edges in graphs:
    # is_sc = all((u, v) in new_edges for u, v in zip(new_topo_order, new_topo_order[1:]))
    # sc.append(1 if is_sc else -1)

    nodes = [u * x for u, x in it.product(vars, [-1, 1])]
    edges = [((-1)*u, v) for u, v in ((e[t], e[(t+1)%2]) for e, t in it.product(edges, range(2)))]
    rev_edges = [(v, u) for u,v in edges]
    topo_order = topo_sort_dfs(nodes, edges)
    parent, reached = dfs(topo_order, rev_edges)[:2]
    reached = sorted(reached.keys(), key=reached.get)
    cnt = it.count()
    comp_map = {c: next(cnt) for c, p in parent.items() if p == None}
    for u in reached:
        if u not in comp_map.keys():
            comp_map[u] = comp_map[parent[u]]
    satisfiable = all(comp_map[v] != comp_map[(-1) * v] for v in vars)
    if not satisfiable:
        print(0)
    else:
        vals = {}
        new_nodes = list(comp_map.values())
        # new_edges = {(comp_map[u], comp_map[v]) for u, v in rev_edges}
        new_edges = {(comp_map[u], comp_map[v]) for u, v in edges}
        new_topo_order = topo_sort_dfs(new_nodes, new_edges)
        for comp in reversed(new_topo_order):
            for x in (x for x, c in comp_map.items() if comp == c):
                v = abs(x)
                if v not in vals:
                    vals[v] = x
        print(1, *sorted(vals.values(), key=abs))

