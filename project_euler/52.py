#!/usr/bin/env python3

from pphelp import *


for n in it.count(1):
    ms = [1, 2, 3, 4, 5, 6]
    ds = {tuple(sorted(digits(m * n))) for m in ms}
    if len(ds) == 1:
        break

print(n)
