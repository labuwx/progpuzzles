#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dna_l = set(from_fasta(ds).values())

dna_m = min(dna_l, key=lambda x: len(x))
l = len(dna_m)
dna_l.remove(dna_m)

# l = 1000
# dna_m = 'a' * l
# dna_l = ['a' * l] * 100 + ['b'*l+'a']

found = False
for j in range(l, -1, -1):
    if found:
        break
    for i in range(0, l - j + 1):
        subs = dna_m[i : i + j]
        found = all((subs in dna) for dna in dna_l)
        if found:
            break

print(subs)
