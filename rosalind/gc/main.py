#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dna = from_fasta(ds)

results = ((name, gc_cont(chain)) for name, chain in dna.items())
winner = max(results, key=lambda x: x[1])

print(winner[0])
print(winner[1])
