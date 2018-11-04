#!/usr/bin/env python3

import heapsort
from bioinf_common import *


ds = get_dataset()
*A, k = [int(x) for x in ds.split()[1:]]

h = heapsort.Heap(A)
l = [h.mindel() for _ in range(k)]

print(*l)
