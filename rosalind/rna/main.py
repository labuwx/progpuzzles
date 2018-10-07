#!/usr/bin/env python3

from bioinf_common import *


dna = get_dataset()
rna = dna2rna(dna)

print(rna)
