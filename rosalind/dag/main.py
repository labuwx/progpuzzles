#!/usr/bin/env python3

from bioinf_common import *


# def acyclic(nodes, edges):
    # edges = set(edges)
    # ends = {e[1] for e in edges}
    # while edges:
        # src = {e[0] for e in edges}
        # leafs = ends - src
        # if not leafs:
            # return False
        # edges -= {e for e in edges if e[1] in leafs}
        # ends -= leafs

    # return True


def acyclic(nodes, edges):
    etype = dfs(nodes, edges)[3]
    dag = not any(e for e, t in etype.items() if t == 'R')
    return dag


ds = get_dataset()
graphs = from_edgelist(ds)

issq = [1 if acyclic(nodes, edges) else -1 for nodes, edges in graphs]
print(*issq)
