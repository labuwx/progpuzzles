#!/usr/bin/env python3

import numpy as np
import itertools as it
from collections import defaultdict, OrderedDict
import math

pprint = __import__('pprint').PrettyPrinter().pprint


def normalize(dir):
    dx, dy = dir
    nf = math.gcd(*dir)
    return (dx // nf, dy // nf), nf


def getdir(ast0, ast):
    return ast[0] - ast0[0], ast[1] - ast0[1]


def grade(asteroids, ast0):
    dirs = set(normalize(getdir(ast0, ast))[0] for ast in asteroids if ast != ast0)
    return len(dirs)


def get_angle(dir):
    dx, dy = dir
    if dx == 0:
        return (0 if dy < 0 else 2, 0)
    else:
        r = dy / dx
        return (1 if dx > 0 else 3, r)


def scan(asteroids, ast0):
    dirmap = defaultdict(list)
    for ast in asteroids:
        if ast == ast0:
            continue
        dir, nf = normalize(getdir(ast0, ast))
        dirmap[dir].append((ast, nf))
    return OrderedDict(
        sorted(
            [
                (d, sorted(al, key=lambda x: x[1], reverse=True))
                for d, al in dirmap.items()
            ],
            key=lambda x: get_angle(x[0]),
        )
    )


def main():
    n = 200
    input = open('input').read().strip().split('\n')
    asteroids = {
        (x, y) for y, l in enumerate(input) for x, c in enumerate(l) if c == '#'
    }

    ast0, s1 = max(
        ((ast, grade(asteroids, ast)) for ast in asteroids), key=lambda x: x[1]
    )

    scmap = scan(asteroids, ast0)
    for al, _ in zip(it.cycle(scmap.values()), range(n)):
        ast1 = al.pop()

    print(s1)
    print(ast1)


main()
