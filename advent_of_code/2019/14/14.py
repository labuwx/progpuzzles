#!/usr/bin/env python3

import itertools as it
import math
import regex as re
from collections import deque


def topo_sort(edgs):
    start_node = 'S_T_A_R_T__N_O_D_E'
    nodes = {e[i] for e in edgs for i in range(2)}
    edges = edgs | {(start_node, x) for x in nodes}
    seen, branch, left = set(), deque(), deque()
    q = deque([start_node])
    while q:
        v = q.pop()
        if v in seen:
            continue
        seen.add(v)
        q.extend(y for x, y in edges if x == v)

        while branch and v not in (y for x, y in edges if x == branch[-1]):
            left.append(branch.pop())
        branch.append(v)
    return list(branch)[1:] + list(left)[::-1]


def ore_req(data, qfuel):
    react_order = topo_sort(
        {(res, ing) for res, (_, ings) in data.items() for ing in ings}
    )
    fumehood = {'FUEL': qfuel}
    for rchem in react_order:
        if rchem not in fumehood or rchem == 'ORE':
            continue
        qneeded = fumehood[rchem]
        nreact = math.ceil(qneeded / data[rchem][0])
        for ichem, iq in data[rchem][1].items():
            fumehood[ichem] = nreact * iq + fumehood.get(ichem, 0)
        del fumehood[rchem]
    assert len(fumehood) == 1
    return fumehood['ORE']


def bin_max_search(lb, ub, pred):
    while lb < ub - 1:
        mid = (lb + ub) // 2
        if pred(mid):
            lb = mid
        else:
            ub = mid
    return ub if pred(ub) else lb


def max_fuel(data, qore):
    ufb = next(2 ** k for k in it.count() if ore_req(data, 2 ** k) >= qore)
    return bin_max_search(1, ufb, lambda x: ore_req(data, x) <= qore)


def parse_chem(s):
    t = s.split(' ')
    return (t[1], int(t[0]))


def main():
    qore = 1000000000000
    input = open('input').read().strip().split('\n')
    rx = re.compile(r'^([, ]*(?P<ing>\d+ \w+)[, ]*)+ *=> *(?P<rq>\d+) (?P<res>\w+)$')
    data = {
        m.group('res'): (
            int(m.group('rq')),
            dict(parse_chem(ing) for ing in m.captures('ing')),
        )
        for m in (rx.match(l.strip()) for l in input)
    }

    s1 = ore_req(data, 1)
    s2 = max_fuel(data, qore)

    print(s1)
    print(s2)


main()
