#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
a, b = [int(x) for x in ds.split()]

s = sum(n for n in range(a, b+1) if n%2)

print(s)


