#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
dna = from_fasta(ds).values()

print(lcsq(*dna))
