#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
s, t = from_fasta(ds).values()

idxs, k = [], 0
for b in t:
    k += s[k+1:].find(b) + 1
    idxs.append(k)

idxs = [i+1 for i in idxs]
print(*idxs)
