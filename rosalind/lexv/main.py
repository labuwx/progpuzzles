#!/usr/bin/env python3

import itertools as it

from bioinf_common import *


ds = get_dataset()
*alphabet, n = ds.split()
n = int(n)

words = it.product(alphabet + ['_'], repeat=n)
words = sorted(
    {''.join(w).replace('_', '') for w in words if w != ('_',) * n},
    key=lambda w: [alphabet.index(c) for c in w],
)

for w in words:
    print(w)
