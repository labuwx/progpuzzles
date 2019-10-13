#!/usr/bin/env python3

from bioinf_common import *


ds = get_dataset()
a, b = [int(x) for x in ds.split()]

c2 = a ** 2 + b ** 2

print(c2)
