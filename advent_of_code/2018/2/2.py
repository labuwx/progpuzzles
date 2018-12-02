#!/usr/bin/env python3

import itertools as it
from collections import Counter


def ham_dist(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


input = open('input').read().split()

cnts = [Counter(l) for l in input]
c2 = sum(any(e[1] == 2 for e in cnt.most_common()) for cnt in cnts)
c3 = sum(any(e[1] == 3 for e in cnt.most_common()) for cnt in cnts)
s1 = c2 * c3

ids = next(ids for ids in it.combinations(input, 2) if ham_dist(*ids) == 1)
s2 = ''.join(c1 for c1, c2 in zip(*ids) if c1 == c2)

print(s1)
print(s2)
