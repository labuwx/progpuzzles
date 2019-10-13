#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dna_l = list(from_fasta(ds).values())

profile = get_profile(dna_l)
consensus = get_consensus(profile)

print(''.join(consensus))
for b, l in profile.items():
    print(b + ':', *l)
