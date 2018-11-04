#!/usr/bin/env python3

from pphelp import *

m = 10 ** 10

s = 0
for n in range(1, 1001):
    s = (s + fastexp(n, n, m)) % m

print(s)
