#!/usr/bin/env python3

from collections import defaultdict
import itertools as it
from math import floor, inf, sqrt


def factors(n):
    p, factors = 2, []
    sqrt_n = floor(sqrt(n))
    while p <= sqrt_n:
        k = 0
        while n % p == 0:
            k += 1
            n //= p
        if k:
            factors.append((p, k))
            sqrt_n = floor(sqrt(n))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def divsum(n):
    fs = factors(n)
    pr = 1
    for d, k in fs:
        pr *= (d ** (k + 1) - 1) // (d - 1)
    return pr


def main():
    input = int(open('input').read().strip())

    s1 = next(n for n in it.count() if 10 * divsum(n) >= input)

    houses = defaultdict(int)
    mhouse = inf
    for i in it.count(1):
        if i > mhouse:
            break
        for j in range(1, 50 + 1):
            h = i * j
            houses[h] += 11 * i
            if houses[h] >= input:
                mhouse = min(mhouse, h)
    s2 = mhouse

    print(s1)
    print(s2)


main()
