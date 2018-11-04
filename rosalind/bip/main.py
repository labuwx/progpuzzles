#!/usr/bin/env python3

from bioinf_common import *


def bipartite(edges):
    color = {}
    for k in {e[0] for e in edges}:
        if k in color.keys():
            continue

        color[k] = 0
        q = deque([k])
        while q:
            u = q.pop()
            c = color[u]
            neighbours = {e[1] for e in edges if e[0] == u}
            if any(v for v in neighbours if color.get(v, None) == c):
                return False
            neighbours = [v for v in neighbours if v not in color.keys()]
            q.extend(neighbours)
            color.update({v: (c+1)%2 for v in neighbours})
    return True


ds = get_dataset()
graphs = [
    {(e[t], e[(t+1)%2]) for e in edges for t in range(2)}
    for _, edges in from_edgelist(ds)
]

isbip = [1 if bipartite(edges) else -1 for edges in graphs]
print(*isbip)
