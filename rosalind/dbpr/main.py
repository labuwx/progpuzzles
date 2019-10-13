#!/usr/bin/env python3

from Bio import ExPASy, SwissProt

from bioinf_common import *


ds = get_dataset()
handle = ExPASy.get_sprot_raw(ds)
record = SwissProt.read(handle)

res = [
    x[2][2:] for x in record.cross_references if x[0] == 'GO' and x[2].startswith('P:')
]
print('\n'.join(res))
