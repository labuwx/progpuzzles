#!/usr/bin/env python3

import math


def parse_input(input):
    ts, ds = (l.split(':')[1].strip() for l in input.strip().split('\n'))

    times = [int(x) for x in ts.split()]
    distances = [int(x) for x in ds.split()]
    T = int(ts.replace(' ', ''))
    D = int(ds.replace(' ', ''))

    return (times, distances), (T, D)


def test(t, d, x):
    return (t - x) * x > d


def main():
    input = open('input').read()
    # input = open('input_test').read()
    (times, distances), (T, D) = parse_input(input)

    s1 = 1
    for t, d in zip(times, distances):
        s1 *= sum(test(t, d, tx) for tx in range(1, t))

    r1 = math.ceil((T - (T**2 - 4 * D) ** (1 / 2)) / 2)
    r2 = math.floor((T + (T**2 - 4 * D) ** (1 / 2)) / 2)
    s2 = (
        math.floor(r2) - math.ceil(r1) + 1 - (not test(T, D, r1)) - (not test(T, D, r2))
    )

    print(s1)
    print(s2)


main()
