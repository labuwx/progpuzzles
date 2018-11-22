#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
p1, p2 = from_fasta(ds).values()

sf = lambda c1, c2: blosum62_scores[(c1, c2)]
edist, _, _ = alignments(p1, p2, gs=-5, sf=sf)
edist = edist

print(edist)
