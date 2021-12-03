#!/usr/bin/env python3

import functools as ft


# TODO: use pandas for most_common and filtering


def tonum(l):
    l = list(l)
    return ft.reduce(lambda acc, x: 2 * acc + x, l, 0)


def most_common(inp, k, break_tie=False):
    n, l = len(inp), len(inp[0])
    c1 = sum(x[k] for x in inp)
    c0 = n - c1

    assert break_tie or c1 != c0
    d = int(c1 >= c0)
    return (d, d if n in [c0, c1] else 1 - d)


def main():
    input = open('input').read().strip()
    input = [tuple(int(d, base=2) for d in x) for x in input.split()]
    n, l = len(input), len(input[0])

    gamma, epsilon = [], []
    oxy_l, co2_l = list(input), list(input)
    for k in range(l):
        dg, de = most_common(input, k)
        gamma.append(dg)
        epsilon.append(de)

        d = most_common(oxy_l, k, break_tie=True)[0]
        oxy_l = [x for x in oxy_l if x[k] == d]

        d = most_common(co2_l, k, break_tie=True)[-1]
        co2_l = [x for x in co2_l if x[k] == d]

    gamma = tonum(gamma)
    epsilon = tonum(epsilon)
    s1 = gamma * epsilon  # power

    oxy = tonum(oxy_l[0])
    co2 = tonum(co2_l[0])
    s2 = oxy * co2  # life support

    print(s1)
    print(s2)


main()
