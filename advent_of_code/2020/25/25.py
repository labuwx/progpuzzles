#!/usr/bin/env python3

import itertools as it


def dlog(base, n, m):
    nt = 1
    for exp in it.count(0):
        if nt == n:
            break
        else:
            nt = (nt * base) % m
    return exp


def main():
    m = 20201227
    input = open('input').read().split()
    k1, k2 = (int(x) for x in input)
    # k1, k2 = 5764801, 17807724

    l2 = dlog(7, k2, m)

    ek = pow(k1, l2, m)
    print(ek)


main()
