#!/usr/bin/env python3


def extrapol(xs, rev=False):
    if rev:
        xs = list(reversed(xs))

    endings = []
    all_zero = False
    while not all_zero:
        all_zero = True
        endings.append(xs[-1])
        nxs = []
        for j in range(len(xs) - 1):
            nx = xs[j + 1] - xs[j]
            all_zero = all_zero and nx == 0
            nxs.append(nx)
        xs = nxs

    return sum(endings)


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = [[int(x) for x in l.split()] for l in input.strip().split('\n')]

    s1 = sum(extrapol(xs, rev=False) for xs in input)
    s2 = sum(extrapol(xs, rev=True) for xs in input)

    print(s1)
    print(s2)


main()
