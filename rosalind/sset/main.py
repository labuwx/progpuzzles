#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
n = int(ds)
m = 1_000_000

n_subs = pow(2, n, m)

print(n_subs)

