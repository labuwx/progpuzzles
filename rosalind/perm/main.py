#!/usr/bin/env python3

from itertools import permutations

from bioinf_common import *


ds = get_dataset()
n = int(ds)

perms = list(permutations(range(1, n+1)))

print(len(perms))
for perm in perms:
    print(*perm)
