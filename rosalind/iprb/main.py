#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
k, m, n = (int(x) for x in ds.split())
s = k + m + n

p = (nCr(k) + k * m + 3 / 4 * nCr(m) + k * n + 1 / 2 * m * n) / nCr(s)

print(p)
