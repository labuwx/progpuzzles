#!/usr/bin/env python3

import itertools as it

from bioinf_common import *


ds = get_dataset()
dna = list(from_fasta(ds).values())[0]

rna_l = [dna2rna(dna), dna2rna(rev_comp(dna))]

results = set()
for rna in rna_l:
    orfs = get_orf(rna)
    prots = (rna2prot(orf) for orf in orfs)
    results.update(prots)

print('\n'.join(results))

