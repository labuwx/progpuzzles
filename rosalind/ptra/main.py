#!/usr/bin/env python3

from Bio.Seq import translate

from bioinf_common import *


ds = get_dataset().split()
dna, prot = ds

idx = next(idx for idx in it.count(1)
           if translate(dna, table=idx, stop_symbol='', to_stop=False) == prot)

print(idx)
print(len(dna))
