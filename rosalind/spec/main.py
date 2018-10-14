#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
L = [float(x) for x in ds.split()]
mmt = monoisotopic_mass_table

W = [w2-w1 for w1, w2 in zip(L, L[1:])]
prot = [min(mmt.keys(), key=lambda aa: abs(w-mmt[aa])) for w in W]

print(''.join(prot))
