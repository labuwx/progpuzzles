#!/usr/bin/env python3

import itertools as it


def josephus(n):
    k = next(i for i in it.count() if 2 ** i > n) - 1
    l = n - 2 ** k
    return 2 * l + 1


def wins2_alt(n):
    res = [None] * (n + 1)
    res[1] = 0
    for k in range(2, n + 1):
        killed = k // 2
        wp = res[k - 1]
        wp = (wp + 1) % (k - 1)
        res[k] = wp if wp < killed else wp + 1

    return res[n] + 1


def wins2(n):
    if n == 1:
        return 1

    k = next(i for i in it.count() if 3 ** i >= n)
    prev_power = 3 ** (k - 1)
    next_power = 3 ** k

    mid = (next_power - prev_power) // 2
    d = n - prev_power
    res = d if d <= mid else mid + (d - mid) * 2

    return res


def main():
    input = int(open('input').read().strip())

    s1 = josephus(input)
    s2 = wins2(input)

    print(s1)
    print(s2)


main()
