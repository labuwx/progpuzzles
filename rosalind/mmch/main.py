#!/usr/bin/env python3

from math import factorial

from bioinf_common import *


ds = get_dataset()
rna = list(from_fasta(ds).values())[0]

na, nc, ng, nu = (rna.count(b) for b in ['A', 'C', 'G', 'U'])
mau, Mau = sorted((na, nu))
mgc, Mgc = sorted((nc, ng))

n_matchings = nCr(Mau, mau)*factorial(mau) * nCr(Mgc, mgc)*factorial(mgc)

print(n_matchings)
