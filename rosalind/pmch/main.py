#!/usr/bin/env python3

from math import factorial

from bioinf_common import *


ds = get_dataset()
rna = list(from_fasta(ds).values())[0]

n_au, n_cg = rna.count('A'), rna.count('C')
n_matchings = factorial(n_au) * factorial(n_cg)

print(n_matchings)
