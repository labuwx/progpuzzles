#!/usr/bin/env python3

from collections import Counter

from bioinf_common import *


ds = get_dataset()
m = 1000000
cnt = Counter(codon_map.values())

res = cnt[None]  # number of stop codons
for aa in ds:
    res = (res * cnt[aa]) % m

print(res)
