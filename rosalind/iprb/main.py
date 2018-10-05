#!/usr/bin/env python3

from sys import argv


def ncr(n):
    return n*(n-1)//2


ds = open(argv[1]).read().strip()
k, m, n = (int(x) for x in ds.split())
s = k + m + n

p = (ncr(k) + k*m + 3/4 * ncr(m) + k*n + 1/2 * m*n ) / ncr(s)

print(p)
