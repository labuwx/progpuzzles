#!/usr/bin/env python3

import mergesort
from bioinf_common import *


ds = get_dataset()
A = [int(x) for x in ds.split()[1:]]

SA = mergesort.sort(A)

print(*SA)
