#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
p1, p2 = from_fasta(ds).values()

sf = lambda c1, c2: -1 if c1 != c2 else 0
_, numal, __ = alignments(p1, p2, gs=-1, sf=sf)

print(numal % 134217727)
