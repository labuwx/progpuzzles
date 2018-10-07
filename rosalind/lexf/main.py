#!/usr/bin/env python3

import itertools as it

from bioinf_common import *


ds = get_dataset()
lines = ds.split('\n')
alphabet = sorted(lines[0].split())
n = int(lines[1])

cmbs = it.product(alphabet, repeat=n)

for cmb in cmbs:
    print(''.join(cmb))
