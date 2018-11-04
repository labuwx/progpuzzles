#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
S = set(ds.split())
# S |= {rev_comp(dna) for dna in S}

edges = {
    (s[:-1], s[1:]) for s in S
}

sstring = next(iter(edges))[0]
k = len(sstring)
for _ in range(len(edges)-k):
    e = next(e for e in edges if e[0] == sstring[-k:])
    sstring += e[1][-1]

print(sstring)
