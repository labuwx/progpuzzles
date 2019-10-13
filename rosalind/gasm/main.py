#!/usr/bin/env python3

import itertools as it

from bioinf_common import *


ds = get_dataset()
S = set(ds.split())
S |= {rev_comp(dna) for dna in S}
S = list(S)
l = len(S[0])

for k in range(1, l):
    Sk = list({s[d : d + k + 1] for s, d in it.product(S, range(l - k))})
    # print(Sk)
    edges = list({(s[:-1], s[1:]) for s in Sk})

    sstring = edges[0][0]
    used_edges = set()
    for _ in range(len(edges) // 2):
        e = next((e for e in edges if e[0] == sstring[-k:]), None)
        if e == None:
            break
        used_edges.add(e)
        sstring += e[1][-1]
    if e != None and sstring[:k] == sstring[-k:] and len(used_edges) == len(edges) // 2:
        # print(k, sstring[k:])
        print(sstring[k:])
        break
