#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dnas = list(from_fasta(ds).values())

r = tt_ratio(*dnas)

print(r)
