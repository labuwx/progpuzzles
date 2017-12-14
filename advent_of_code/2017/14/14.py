#!/usr/bin/env python3

import functools as ft
import itertools as it
import numpy as np


def rounder(input, nround=1):
    l = 256
    mem = list(range(l))
    idx = skip = 0
    for _ in range(nround):
        for n in input:
            for j in range(n // 2):
                i1 = (idx+j) % l
                i2 = (idx+n-1-j) % l
                mem[i1], mem[i2] = mem[i2], mem[i1]
            idx = (idx + n + skip) % l
            skip += 1
    return mem


def hash(input):
    input = list(map(ord, input))
    input += [17, 31, 73, 47, 23]
    mem = rounder(input, 64)
    dense_mem = [ft.reduce(lambda x, y: x^y, mem[i*16: i*16+16]) for i in range(16)]
    return ft.reduce(lambda x, y: 256*x + y, dense_mem)


def neighbours(coll, p):
    p1, p2 = p
    ds = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    ng = [coll.get((p1+d1, p2+d2), None) for d1, d2 in ds]
    ng = [x for x in ng if x != None]
    return ng


input = 'jzgqcdpd'
#input = 'flqrgnkx'

disk = np.asarray([[int(b) for b in format(hash(input + '-%d' % i), 'b').zfill(128)] for i in range(128)])
num_ones = disk.sum()

regs = {(i, j): (i, j) for i, j in it.product(range(128), range(128)) if disk[i, j] == 1}
change = True
while change:
    change = False
    for p in regs.copy():
        v = regs[p]
        v_min = min(neighbours(regs, p))
        if v_min < v:
            change = True
            regs[p] = v_min

num_regs = len(set(regs.values()))

print(num_ones)
print(num_regs)
