#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
rna = dna2rna(ds)

orfs = get_orf(rna) + get_orf(rev_comp_rna(rna))
orf = max(orfs, key=len)
res = rna2prot(orf)

print(res)
