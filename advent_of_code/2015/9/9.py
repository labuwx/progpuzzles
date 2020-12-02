#!/usr/bin/env python3

import itertools as it


def cost(dists, path):
    c = sum(dists[p] for p in zip(path, path[1:]))
    return c


def main():
    input = open('input').read().strip().split('\n')

    dists, cities = {}, set()
    for l in input:
        a, _, b, _, c = l.split()
        cities.update({a, b})
        dists[(a, b)] = dists[(b, a)] = int(c)

    s1 = min(cost(dists, path) for path in it.permutations(cities))
    s2 = max(cost(dists, path) for path in it.permutations(cities))

    print(s1)
    print(s2)


main()
