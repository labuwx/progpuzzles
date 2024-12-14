#!/usr/bin/env python3

from collections import defaultdict
import itertools as it
import math
import numpy as np
import re


def tadd(x, y, t=1):
    return tuple(xx + t * yy for xx, yy in zip(x, y))


def var(robots):
    return np.var(robots, axis=0)


def print_bots(S, robpos):
    txt = [[' ' for _ in range(S[0])] for _ in range(S[1])]
    for x, y in robpos:
        txt[y][-x - 1] = '#'
    print('\n'.join(''.join(l) for l in txt))


rx = r'p=(?P<PX>-?\d+),(?P<PY>-?\d+) v=(?P<VX>-?\d+),(?P<VY>-?\d+)'


def main():
    input, S = open('input').read(), (101, 103)
    # input, S = open('input_test').read(), (11, 7)
    N = 100
    S2 = (S[0] // 2, S[1] // 2)

    robots = [
        ((int(m['PX']), int(m['PY'])), (int(m['VX']), int(m['VY'])))
        for m in re.finditer(rx, input)
    ]

    Q = defaultdict(int)
    for p, v in robots:
        pn = tuple(pi % s for pi, s in zip(tadd(p, v, N), S))
        if any(pni == s2i for pni, s2i in zip(pn, S2)):
            continue
        Q[tuple(pni <= s2i for pni, s2i in zip(pn, S2))] += 1

    s1 = math.prod(Q.values())
    print(s1)

    robpos = [pos for pos, _ in robots]
    v = var(robpos)
    for k in it.count(1):

        for r, (_, velo) in enumerate(robots):
            robpos[r] = tuple(pi % s for pi, s in zip(tadd(robpos[r], velo), S))

        vn = var(robpos)
        if np.all(vn < 0.5 * v):
            print(k)
            print()
            print_bots(S, robpos)
            break
        else:
            v = (v + vn) / 2


main()
