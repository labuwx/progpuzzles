#!/usr/bin/env python3

import itertools as it
from collections import defaultdict


def next_point(p):
    p1, p2 = p
    r = max(map(abs, p))

    if p1 == -p2 == r:
        return p1 + 1, p2
    if p1 == r and p2 < r:
        return p1, p2 + 1
    if p2 == r and -r < p1:
        return p1 - 1, p2
    if p1 == -r and -r < p2:
        return p1, p2 - 1
    if p2 == -r:
        return p1 + 1, p2

    assert False


def neighbours(p):
    p1, p2 = p
    d = [0, -1, 1]
    return [(p1 + d1, p2 + d2) for d1, d2 in it.product(d, d)][1:]


input = 347991


p = (0, 0)
for _ in range(input - 1):
    p = next_point(p)
print(sum(map(abs, p)))


t = defaultdict(int)
p = (0, 0)
v = t[p] = 1

while v <= input:
    p = next_point(p)
    v = sum(t[q] for q in neighbours(p))
    t[p] = v

print(v)
