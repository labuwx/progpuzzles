#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
S = set(ds.split())
S |= {rev_comp(dna) for dna in S}

edges = {
    (s[:-1], s[1:]) for s in S
}

for e in edges:
    print(r'(%s, %s)' % e)
