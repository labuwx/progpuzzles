#!/usr/bin/env python3

import itertools as it
import re
import numpy as np
from collections import deque


def tbt(s):
    return tuple(c == '#' for c in s)


def get_window(T, im, wsize, idx):
    window = tuple(
        T[i - im] if (i - im) in range(len(T)) else False
        for i in range(idx - wsize//2, idx + wsize//2 + 1)
    )
    return window


def get_gener(cache, sT, sim, n):
    hs = tuple(sT)
    n0, im0 = cache[hs]
    if n < n0:
        return next((iim, t) for t, (nn, iim) in cache.items() if nn == n)
    else:
        plen = len(cache) - n0
        nm = (n - n0) % plen
        t, (nn, iim) = next(x for x in cache.items() if x[1][0] == (nm + n0))
        pc = (n - nn) // plen
        iiim = iim + pc * (sim - im0)

        return (iiim, t)


rx = re.compile(r'^(?P<pattern>[#.]+) => (?P<res>[#.])$')
input = open('input').read().strip().split('\n')
n1, n2 = 20, 50000000000

init = tbt(re.match(r'^initial state: (?P<init>[#.]+)$', input[0]).group('init'))

rules = {
    tbt(m.group('pattern')) : tbt(m.group('res'))[0]
    for m in (rx.match(l) for l in input[2:])
}
wsize = len(next(iter(rules.keys())))
assert rules[(False,) * wsize] == False

im, T, cache = 0, deque(init), {}
for n in it.count():
    hs = tuple(T)
    if hs in cache:
        break
    else:
        cache[hs] = (n, im)

    df = wsize // 2
    T = deque(rules[get_window(T, im, wsize, i)] for i in range(im - df, im + len(T) + df))
    im -= df
    while T[-1] == False: T.pop()
    while T[0] == False:
        T.popleft()
        im += 1

im1, T1 = get_gener(cache, T, im, n1)
s1 = sum(i + im1 for i, p in enumerate(T1) if p)

im2, T2 = get_gener(cache, T, im, n2)
s2 = sum(i + im2 for i, p in enumerate(T2) if p)

print(s1)
print(s2)
