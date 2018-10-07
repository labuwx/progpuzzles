#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dna = list(from_fasta(ds).values())[0]
l = len(dna)

for j in range(4, 12+1, 2):
    for i in range(0, l-j+1):
        subs = dna[i:i+j]
        if subs == rev_comp(subs):
            print(i+1, j)
