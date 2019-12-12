#!/usr/bin/env python3

import functools as ft
import itertools as it
import math
import re
from copy import deepcopy


def add(a, b):
    return tuple(ai + bi for ai, bi in zip(a, b))


def absum(v):
    return sum(abs(x) for x in v)


def cmp(a, b):
    return 1 if a < b else (0 if a == b else -1)


def cmpv(a, b):
    return tuple(cmp(ai, bi) for ai, bi in zip(a, b))


def pull(data):
    for m1, m2 in it.combinations(data, 2):
        m1[1] = add(m1[1], cmpv(m1[0], m2[0]))
        m2[1] = add(m2[1], cmpv(m2[0], m1[0]))


def move(data):
    for moon in data:
        moon[0] = add(moon[0], moon[1])


def simul(data, nsteps=1):
    for _ in range(nsteps):
        pull(data)
        move(data)


def energy(data):
    return sum(absum(m[0]) * absum(m[1]) for m in data)


def freeze_state(data):
    return tuple(
        tuple(tuple(par[k] for par in moon) for moon in data) for k in range(ndim)
    )


def lcm(numbers):
    return ft.reduce(lambda x, y: (x * y) // math.gcd(x, y), numbers, 1)


def calc_cycle(cycles):
    cyc_len = lcm(cyc[1] for cyc in cycles)
    start = max(cyc[0] for cyc in cycles)
    return start, cyc_len


def main():
    global ndim
    nit = 1000
    ndim = 3
    input = open('input').read().strip().split('\n')
    rx = re.compile(r'^<x=(?P<px>-?\d+),\s*y=(?P<py>-?\d+),\s*z=(?P<pz>-?\d+)>$')
    data = [
        [(int(m.group('px')), int(m.group('py')), int(m.group('pz'))), (0, 0, 0)]
        for m in (rx.match(l.strip()) for l in input)
    ]

    data1 = deepcopy(data)
    simul(data1, nit)
    s1 = energy(data1)

    data2 = deepcopy(data)
    states = tuple({} for _ in range(ndim))
    cycles = [None for _ in range(ndim)]
    for i in it.count():
        cstate = freeze_state(data2)
        ha = True
        for k, (st, sts) in enumerate(zip(cstate, states)):
            # print('hi')
            if cycles[k] != None:
                continue
            ha = False
            if st in sts:
                cycles[k] = (sts[st], i - sts[st])
            else:
                sts[st] = i
        if ha:
            break

        simul(data2)
    s2 = sum(calc_cycle(cycles))

    print(s1)
    print(s2)


main()
