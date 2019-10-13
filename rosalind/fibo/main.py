#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
n = int(ds)

a, b = 0, 1
for _ in range(n - 1):
    a, b = b, a + b

print(b)
