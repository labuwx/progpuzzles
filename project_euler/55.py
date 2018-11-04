#!/usr/bin/env python3

from pphelp import *


n_lychrel = sum(1 for n in range(10000) if is_lychrel(n))

print(n_lychrel)
