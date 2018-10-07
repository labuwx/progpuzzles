#!/usr/bin/env python3

import itertools as it

from bioinf_common import *


ds = get_dataset()
dna = from_fasta(ds)

edges = [
    (n1, n2)
    for (n1, c1), (n2, c2) in it.permutations(dna.items(), 2)
    if c1[-3:] == c2[:3]
]

for edge in edges:
    print(*edge)

