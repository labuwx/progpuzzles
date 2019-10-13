#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
n, m = (int(x) for x in ds.split())
mod = 1_000_000

res = sum(nCr(n, k) for k in range(m, n + 1)) % mod

print(res)
