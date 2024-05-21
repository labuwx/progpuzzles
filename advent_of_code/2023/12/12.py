#!/usr/bin/env python3


import itertools as it


def calc(p, r):
    # patternize
    r = '*' + '.*'.join('#' * int(rx) for rx in r.split(',')) + '*'

    Fp = [1, 1] + [0] * (len(r) - 1)
    for pi in p:
        F = [0] * len(Fp)

        for j, rj in zip(it.count(1), r):

            match rj + pi:
                case '..' | '##' | '#?' | '.?':
                    x = Fp[j - 1]
                case '.#' | '#.':
                    x = 0
                case '*#':
                    x = F[j - 1]
                case '*.' | '*?':
                    x = Fp[j] + F[j - 1]

            F[j] = x

        Fp = F

    return F[-1]


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = input.strip().split('\n')

    PR1, PR5 = [], []
    for l in input:
        p, r = l.split()
        p5 = '?'.join([p] * 5)
        r5 = ','.join([r] * 5)
        PR1.append((p, r))
        PR5.append((p5, r5))

    s1 = sum(calc(*pr) for pr in PR1)
    s2 = sum(calc(*pr) for pr in PR5)

    print(s1)
    print(s2)


main()
