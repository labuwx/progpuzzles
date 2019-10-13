#!/usr/bin/env python3

from pphelp import *


p = 0
for n in it.count(1, 2):
    corners = [n ** 2 + n + 1 + i * (n + 1) for i in range(3)]
    p += sum(1 for x in corners if isprime(x))
    if p < 0.1 * (2 * (n + 1) + 1):
        break

print(n + 2)
