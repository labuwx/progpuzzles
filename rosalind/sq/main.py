#!/usr/bin/env python3

from bioinf_common import *


def sq(edges):
    seen = set()
    for k in {e[0] for e in edges}:
        if k in seen:
            continue

        q = deque([(k,)])
        seen.add(k)
        while q:
            p = q.pop()
            neighbours = {e[1] for e in edges if e[0] == p[-1]}
            q.extend((v,) for v in neighbours if v not in seen)
            seen.update(neighbours)

            if len(p) == 4:
                if p[0] in neighbours:
                    # print(p)
                    return True
            else:
                q.extend(p + (v,) for v in neighbours if v not in p)
    return False


ds = get_dataset()
graphs = [
    {(e[t], e[(t+1)%2]) for e in edges for t in range(2)}
    for _, edges in from_edgelist(ds)
]

issq = [1 if sq(edges) else -1 for edges in graphs]
print(*issq)
