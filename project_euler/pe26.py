#!/usr/bin/env python3


def lr(d):
    nl = []
    n = 1
    while n and n not in nl:
       nl.append(n)
       n = (n % d) * 10
    return len(nl) - nl.index(n) if n else 0


mv = 0
for d in range(2, 1000):
    l = lr(d)
    if l > mv:
        mk = d
        mv = l

print(mk)

