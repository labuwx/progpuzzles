#!/usr/bin/env python3

import itertools as it

from bioinf_common import *


ds = get_dataset()
A = [int(x) for x in ds.split()[1:]]

inv = sum(1 for x, y in it.combinations(A, 2) if x > y)

print(inv)
