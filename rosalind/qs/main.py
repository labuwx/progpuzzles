#!/usr/bin/env python3

import quicksort
from bioinf_common import *


ds = get_dataset()
A = [int(x) for x in ds.split()[1:]]

l = quicksort.sort(A)

print(*l)
