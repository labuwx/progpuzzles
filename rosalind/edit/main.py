#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
p1, p2 = from_fasta(ds).values()

edist = edit_distance(p1, p2)
print(edist)
