#!/usr/bin/env python3

import itertools as it
import numpy as np


dirs = [(x, y) for x, y in it.product([-1, 0, 1], repeat=2) if not x == 0 == y]

# floor, empty, occupied
CO, CT, CL = '.', '|', '#'


def cadd(*args):
    return tuple(sum(coords) for coords in zip(*args))


def inrange(a, b, c):
    return all(ai <= bi < ci for ai, bi, ci in zip(a, b, c))


def neighbours(land, pos):
    nt, nl = 0, 0
    for d in dirs:
        npos = cadd(pos, d)
        if not inrange((0, 0), npos, land.shape):
            continue
        if land[npos] == CT:
            nt += 1
        elif land[npos] == CL:
            nl += 1

    return nt, nl


def freeze(land):
    return tuple(x for _, x in np.ndenumerate(land))


def collect(land):
    l, seen = [], {}
    for i in it.count():
        n_tree, n_lumber = 0, 0
        new_land = np.empty_like(land)
        for pos, x in np.ndenumerate(land):
            nb_tree, nb_lumber = neighbours(land, pos)
            if x == CO:
                v = CT if nb_tree >= 3 else CO
            elif x == CT:
                n_tree += 1
                v = CL if nb_lumber >= 3 else CT
            elif x == CL:
                n_lumber += 1
                v = CL if nb_lumber >= 1 and nb_tree >= 1 else CO
            new_land[pos] = v

        if (st := freeze(land)) in seen:
            k = seen[st]
            break
        else:
            seen[st] = i
            l.append(n_tree * n_lumber)
        land = new_land

    return tuple(l[:k]), tuple(l[k:])


def seq_idx(seq, i):
    prefix, rep = seq
    if i < len(prefix):
        return prefix[i]
    else:
        return rep[(i - len(prefix)) % len(rep)]


def main():
    input = open('input').read().split()
    shape = (len(input[0]), len(input))

    land = np.fromfunction(np.vectorize(lambda x, y: input[y][x]), shape, dtype=object)

    seq = collect(land)
    s1 = seq_idx(seq, 10)
    s2 = seq_idx(seq, 1000000000)

    print(s1)
    print(s2)


main()
