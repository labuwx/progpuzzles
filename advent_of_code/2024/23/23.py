#!/usr/bin/env python3

from collections import defaultdict
import itertools as it


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = [tuple(l.split('-')) for l in input.strip().splitlines()]

    G = defaultdict(set)
    for u, v in input:
        G[u].add(v)
        G[v].add(u)

    trs = set()
    s2 = None
    for u, nus in G.items():
        if u.startswith('t'):
            for v, w in it.combinations(nus, 2):
                if w in G[v]:
                    trs.add(tuple(sorted((u, v, w))))

        # assumes: G is d-regular and the size of the maximum clique is d
        if s2 is None:
            ptn = [v for v in nus if len(nus & G[v]) == len(nus) - 2]
            if len(ptn) == len(nus) - 1:
                s2 = [u, *ptn]

    s1 = len(trs)
    s2 = ','.join(sorted(s2))

    print(s1)
    print(s2)


main()
