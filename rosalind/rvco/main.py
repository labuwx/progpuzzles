#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dnas = from_fasta(ds).values()

res = sum(1 for dna in dnas if dna == rev_comp(dna))

print(res)
