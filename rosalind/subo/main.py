#!/usr/bin/env python3

from collections import defaultdict
import itertools as it

from bioinf_common import *


def lalign(a, b):
    la, lb = len(a), len(b)
    cache = defaultdict(lambda: ('', '', 0))
    for i, j, mmt in it.product(range(la), range(lb), range(0 + 1)):
        if a[i] == b[j]:
            sa, sb, scr = cache[(i - 1, j - 1, mmt)]
            cache[(i, j, mmt)] = (sa + a[i], sb + b[j], scr + 1)
        elif mmt == 0:
            cache[(i, j, mmt)] == ('', '', 0)
        else:
            sa, sb, scr = cache[(i - 1, j - 1, mmt - 1)]
            sa1, sb1, scr1 = cache[(i - 1, j, mmt - 1)]
            sa2, sb2, scr2 = cache[(i, j - 1, mmt - 1)]
            if scr1 <= scr and scr2 <= scr:
                cache[(i, j, mmt)] = (sa + a[i], sb + b[j], scr)
            elif scr2 <= scr1:
                cache[(i, j, mmt)] = (sa1 + a[i], sb1 + '_', scr1)
            else:
                cache[(i, j, mmt)] = (sa2 + '_', sb2 + b[j], scr2)
    res = max(cache.values(), key=lambda x: x[-1])[:2]

    return res


def count(s, p):
    mmt = 4
    s += '_' * mmt
    c = 0
    for i in range(len(s) - len(p) + 1):
        mm = 0
        for j in range(len(p)):
            if s[i + j] != p[j]:
                mm += 1
            if mm > mmt:
                break
        if mm <= mmt:
            c += 1

    return c


ds = get_dataset()
c1, c2 = from_fasta(ds).values()

p1, p2 = lalign(c1, c2)
n1, n2 = count(c1, p1), count(c2, p2)

print(p1, p2)
print(n1, n2)
