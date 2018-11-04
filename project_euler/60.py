#!/usr/bin/env python3

from pphelp import *

pcheck = eratosthenes_sieve(40_000_000)
primes = [p for p, v in enumerate(pcheck) if v and p < 30000]
print('Primes done.')

for s in it.count(3, 2):
    print(s)
    for a in range(3, s):
        if not primes[a]: continue
        for b in range(a, s-a):
            if not primes[b]: continue
            for c in range(b, s-a-b):
                if not primes[c]: continue
                for d in range(c, s-a-b-c):
                    if not primes[d]: continue
                    e = s - a - b - c - d
                    if e < 2 or not primes[e]: continue
                    ps = [a, b, c, d, e]
                    if all(primes[tonum(digits(p1) + digits(p2))] for p1, p2 in it.permutations(ps, 2)):
                        print(s)
                        exit()
