#!/usr/bin/env python3

from pphelp import *

primes = {2}  # 2 is never needed
for n in it.count(3, 2):
    if isprime(n):
        primes.add(n)
    else:
        goldbach = any((n - 2 * k**2) in primes for k in range(1, int((n/2) ** 0.5) + 1))
        if not goldbach:
            print(n)
            break


