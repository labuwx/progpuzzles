#!/usr/bin/env python3

import itertools as it
from collections import Counter


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


input = open('input').read().strip().split('\n')
input = [tuple(int(x) for x in l.replace(',', '').split()) for l in input]
slim = 10000

xmin, xmax = min(p[0] for p in input), max(p[0] for p in input)
ymin, ymax = min(p[1] for p in input), max(p[1] for p in input)

T, fins, s2 = {}, set(range(len(input))), 0
for p in it.product(
    range(xmin, xmax + 1), range(ymin, ymax + 1)
):  # might need to extend the range for the second part
    ds = {i: dist(p0, p) for i, p0 in enumerate(input)}
    s2 += sum(ds.values()) < slim
    min_dist = min(d for d in ds.values())
    dom = {i for i, d in ds.items() if d == min_dist}
    T[p] = ds, dom

    if len(dom) == 1 and (p[0] == xmin or p[0] == xmax or p[1] == ymin or p[1] == ymax):
        fins -= dom

cnt = Counter()
for v in T.values():
    dom = list(v[1])
    if len(dom) == 1 and dom[0] in fins:
        cnt[dom[0]] += 1

s1 = cnt.most_common(1)[0][1]

print(s1)
print(s2)
