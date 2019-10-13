#!/usr/bin/env python3

from pphelp import *

for x, d in it.product(range(1009, 9999), range(2, 5000)):
    y, z = x + d, x + 2 * d
    if (
        z < 10000
        and isprime(x)
        and isprime(y)
        and isprime(z)
        and sorted(str(x)) == sorted(str(y)) == sorted(str(z))
        and [x, y, z] != [1487, 4817, 8147]
    ):
        print(str(x) + str(y) + str(z))
        break
