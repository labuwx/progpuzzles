#!/usr/bin/env python3

from collections import Counter

from bioinf_common import *


ds = get_dataset()
m = 1000000
cnt = Counter(codon_map.values())

res = cnt[None]  # number of stop codons
for prot in ds:
    res = (res * cnt[prot]) % m

print(res)
