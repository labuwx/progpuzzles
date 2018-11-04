#!/usr/bin/env python3

from pphelp import *

primes = [p for p in range(2, 1_000_000) if isprime(p)]
pcheck = set(primes)
l = len(primes)

found = False
for n in range(l, 0, -1):
    if found: break
    for i in range(l - n + 1):
        s = sum(primes[i: i+n])
        if s >= 1_000_000: break
        if s in primes:
            print(s)
            found = True
            break
