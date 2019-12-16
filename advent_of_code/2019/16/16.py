#!/usr/bin/env python3

import numpy as np


def fft(pattern, nphase, v):
    n, k = len(v), len(pattern)
    patter_exp = np.array(
        [
            np.pad(np.repeat(pattern, i + 1), (0, max(0, n)), mode='wrap')[1 : n + 1]
            for i in range(n)
        ]
    )
    for _ in range(nphase):
        t = v * patter_exp
        t = t.sum(axis=1)
        v = np.vectorize(lambda x: abs(x) % 10)(t)
    return v


def main():
    nphase = 100
    pattern = np.array([0, 1, 0, -1])
    input = np.array([int(digit) for digit in open('input').read().strip()])

    s1 = ''.join(str(d) for d in fft(pattern, nphase, input)[:8])

    print(s1)


main()
