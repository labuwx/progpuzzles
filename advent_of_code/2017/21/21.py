#!/usr/bin/env python3

import numpy as np
import re
import itertools as it


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def t2a(x):
    l = isqrt(len(x))
    return np.asarray(x).reshape((l, l))


def a2t(x):
    return tuple(x.flatten())


def fpat(x):
    for r, m in it.product(range(4), range(2)):
        f = a2t(np.rot90(np.flipud(x) if m else x, r))
        t = patterns.get(f, None)
        if t != None:
            return t2a(t)
    assert False


input = open('input').read()

patterns = {}
for line in input.split('\n'):
    if line == '':
        continue
    m = re.match(r'^(?P<from>[.#/]+) => (?P<to>[.#/]+)$', line)
    frm = tuple(1 if c == '#' else 0 for c in m.group('from') if c != '/')
    to = tuple(1 if c == '#' else 0 for c in m.group('to') if c != '/')
    patterns[frm] = to


art = t2a((0, 1, 0, 0, 0, 1, 1, 1, 1))
for m in range(18):
    ps = 3 if art.shape[0] % 2 else 2
    n = art.shape[0] // ps
    art_new = np.empty((n * (ps + 1), n * (ps + 1)), int)
    for i, j in it.product(range(n), range(n)):
        f = art[i * ps : (i + 1) * ps, j * ps : (j + 1) * ps]
        t = fpat(f)
        art_new[
            i * (ps + 1) : (i + 1) * (ps + 1), j * (ps + 1) : (j + 1) * (ps + 1)
        ] = t
    art = art_new
    if m + 1 == 5:
        c5 = art.sum()
    elif m + 1 == 18:
        c18 = art.sum()

print(c5)
print(c18)
