#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dnas = list(from_fasta(ds).values())

n = len(dnas[0])

for s1 in dnas:
    row = (hamm_dist(s1, s2) / n for s2 in dnas)
    print(*row)
