#!/usr/bin/env python3

from collections import Counter

from bioinf_common import *


ds = get_dataset()
chains = list(from_fasta(ds).values())
cnt = Counter(chains)

correct = set()
incorrect = []
for c in chains:
    rc = rev_comp(c)
    n = cnt[c] + cnt[rc]
    if n == 1:
        incorrect.append(c)
    else:
        correct.update({c, rc})

for c in incorrect:
    oc = next(oc for oc in correct if hamm_dist(c, oc) == 1)
    print(r'%s->%s' % (c, oc))
