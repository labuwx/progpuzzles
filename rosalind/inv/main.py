#!/usr/bin/env python3

import mergesort
from bioinf_common import *


ds = get_dataset()
A = [int(x) for x in ds.split()[1:]]

inv = mergesort.sort(A, report_inv=True)[1]

print(inv)
