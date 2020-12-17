#!/usr/bin/env python3

from collections import Counter
import itertools as it


def gen_dirs(ndim):
    dirs = [
        pos for pos in it.product([-1, 0, 1], repeat=ndim) if any(pi != 0 for pi in pos)
    ]
    return dirs


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def simulate(cubes0, n_steps, ndim):
    dirs = gen_dirs(ndim)
    cubes = {p + (0,) * (ndim - len(p)) for p in cubes0}

    for _ in range(n_steps):
        neighbors = Counter()
        for pos in cubes:
            for dir in dirs:
                neighbors[cadd(pos, dir)] += 1
        cubes = {
            pos
            for pos, nc in neighbors.items()
            if (pos in cubes and 2 <= nc <= 3) or (pos not in cubes and nc == 3)
        }

    return cubes


def main():
    input = open('input').read().split()
    cubes0 = {(x, y) for y, l in enumerate(input) for x, c in enumerate(l) if c == '#'}
    n_steps = 6

    s1 = len(simulate(cubes0, n_steps, 3))
    s2 = len(simulate(cubes0, n_steps, 4))

    print(s1)
    print(s2)


main()
