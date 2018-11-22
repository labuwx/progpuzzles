#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
p1, p2 = from_fasta(ds).values()

sf = lambda c1, c2: -1 if c1 != c2 else 0
edist, _, ag = alignments(p1, p2, gs=-1, sf=sf)
edist = 0 - edist
al = next(ag)

print(edist)
print('\n'.join(al).replace('_', '-'))
