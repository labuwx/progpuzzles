#!/usr/bin/env python3


def cs(a, m):
    a = a % m
    x = (a * a) % m
    l = [a]
    while x not in l:
        l.append(x)
        x = (x * a) % m
    offset = l.index(x)
    cyc_len = len(l) - offset
    return offset, cyc_len


m = 4
for i in range(m):
    print(i, cs(i, m))
