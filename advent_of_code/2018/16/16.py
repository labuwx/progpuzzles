#!/usr/bin/env python3

import itertools as it
import re
from copy import deepcopy

pprint = __import__('pprint').PrettyPrinter().pprint


def rcpm(r, i, v):
    r = list(r)
    r[i] = v
    return tuple(r)


OPS = {
    'addr': (lambda r, a, b, c: rcpm(r, c, r[a] + r[b])),
    'addi': (lambda r, a, b, c: rcpm(r, c, r[a] + b)),
    'mulr': (lambda r, a, b, c: rcpm(r, c, r[a] * r[b])),
    'muli': (lambda r, a, b, c: rcpm(r, c, r[a] * b)),
    'banr': (lambda r, a, b, c: rcpm(r, c, r[a] & r[b])),
    'bani': (lambda r, a, b, c: rcpm(r, c, r[a] & b)),
    'borr': (lambda r, a, b, c: rcpm(r, c, r[a] | r[b])),
    'bori': (lambda r, a, b, c: rcpm(r, c, r[a] | b)),
    'setr': (lambda r, a, b, c: rcpm(r, c, r[a])),
    'seti': (lambda r, a, b, c: rcpm(r, c, a)),
    'gtir': (lambda r, a, b, c: rcpm(r, c, int(a > r[b]))),
    'gtri': (lambda r, a, b, c: rcpm(r, c, int(r[a] > b))),
    'gtrr': (lambda r, a, b, c: rcpm(r, c, int(r[a] > r[b]))),
    'eqir': (lambda r, a, b, c: rcpm(r, c, int(a == r[b]))),
    'eqri': (lambda r, a, b, c: rcpm(r, c, int(r[a] == b))),
    'eqrr': (lambda r, a, b, c: rcpm(r, c, int(r[a] == r[b]))),
}


def revmap(map):
    new_keys = set()
    for v in map.values():
        new_keys |= v
    rmap = {k: set() for k in new_keys}
    for k, v in map.items():
        for nk in v:
            rmap[nk].add(k)
    return rmap


def find_bijection(map):
    map = deepcopy(map)
    change = True
    for i in it.count():
        rmap = revmap(map)
        singles = {k: next(iter(v)) for k, v in rmap.items() if len(v) == 1}
        change = False
        for k, v in singles.items():
            change |= len(map[v]) > 1
            map[v] = {k}
        # for k, v in map.items():
            # if len(v) != 1: continue
            # v = next(iter(v))
            # for k2, v2 in map.items():
                # if k2 != k and v in v2:
                    # change = True
                    # v2.remove(v)
        map = revmap(map)
        if not change: break
    return map if i % 2 else revmap(map)
    # return map


rex = r'''Before: \s+\[(?P<b0>\d+), \s(?P<b1>\d+), \s(?P<b2>\d+), \s(?P<b3>\d+)\]\n
(?P<op>\d+) \s(?P<a>\d+) \s(?P<b>\d+) \s(?P<c>\d+)\n
After: \s+\[(?P<a0>\d+), \s(?P<a1>\d+), \s(?P<a2>\d+), \s(?P<a3>\d+)\]'''

input1, input2 = open('input').read().split('\n\n\n')

omap = {i: set(OPS.keys()) for i in range(len(OPS))}

s1 = 0
for sample in re.finditer(rex, input1, flags=re.VERBOSE):
    rb = tuple(int(sample['b%d' % i]) for i in range(4))
    ra = tuple(int(sample['a%d' % i]) for i in range(4))
    opc, a, b, c = (int(sample[x]) for x in ('op', 'a', 'b', 'c'))
    passed = set()
    for op, f in OPS.items():
        try:
            if ra == f(rb, a, b, c):
                passed.add(op)
        except:
            pass
    omap[opc] &= passed
    s1 += len(passed) >= 3

print(s1)
# pprint(omap)
omap = find_bijection(omap)
pprint(omap)

input2 = [tuple(int(x) for x in l.split()) for l in input2.strip().split('\n')]
r = [0] * 4
for opc, a, b, c in input2:
    f = OPS[next(iter(omap[opc]))]
    r = f(r, a, b, c)
s2 = r[0]
print(s2)
