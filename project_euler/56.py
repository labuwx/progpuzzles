#!/usr/bin/env python3

from pphelp import *


ds = max(sum(digits(a**b)) for a, b in it.product(range(1, 100), repeat=2))

print(ds)
