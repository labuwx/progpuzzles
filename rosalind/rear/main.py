#!/usr/bin/env python3

import itertools as it
from collections import deque, defaultdict

from bioinf_common import *


def revp(p, i, j):
    a, b, c = p[:i], p[i : j + 1], p[j + 1 :]
    q = a + tuple(reversed(b)) + c
    return q


def revd(p1, p2):
    l = len(p1)
    p1 = tuple(p2.index(x) for x in p1)
    p2 = tuple(range(l))

    seen = {p1}
    q = deque([(p1, 0)])
    while q:
        p, d = q.popleft()
        if p == p2:
            return d
        # if d == 9: continue
        endpoint = defaultdict(
            lambda: (False, False),
            {
                i: (
                    i == 0 or abs(p[i - 1] - x) > 1,
                    i == l - 1 or abs(p[i + 1] - x) > 1,
                )
                for i, x in enumerate(p)
            },
        )
        for i, j in it.combinations(range(l), 2):
            if not (endpoint[i][0] and endpoint[j][1]):
                continue
            pp = revp(p, i, j)
            if pp not in seen:
                seen.add(pp)
                q.append((pp, d + 1))


ds = get_dataset()
perms = [tuple(int(x) for x in l.split()) for l in ds.split('\n') if l]
ppairs = [(p1, p2) for p1, p2 in zip(perms[::2], perms[1::2])][:]

dists = [revd(*p) for p in ppairs]

print(*dists)
