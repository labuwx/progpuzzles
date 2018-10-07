#!/usr/bin/env python3

from collections import deque

from bioinf_common import *


ds = get_dataset()
n, m = (int(x) for x in ds.split())

pop = deque([0] * (m-1) + [1], m)

s = 1
for i in range(1, n):
    new_born = s - pop[-1]
    pop.popleft()
    pop.append(new_born)
    s = sum(pop)

print(s)

