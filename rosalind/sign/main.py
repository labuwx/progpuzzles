#!/usr/bin/env python3

import itertools as it
from math import factorial

from bioinf_common import *


ds = get_dataset()
n = int(ds)
n_perm = factorial(n) * 2**n

print(n_perm)

for perm, signs in it.product(it.permutations(range(1, n+1)), it.product([-1, 1], repeat=n)):
    signed_perm = (x*y for x, y in zip(perm, signs))
    print(*signed_perm)
