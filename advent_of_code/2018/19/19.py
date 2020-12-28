#!/usr/bin/env python3

import math


def factors(n):
    p, factors = 2, []
    sqrt_n = math.floor(math.sqrt(n))
    while p <= sqrt_n:
        k = 0
        while n % p == 0:
            k += 1
            n //= p
        if k:
            factors.append((p, k))
            sqrt_n = math.floor(math.sqrt(n))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def divsum(n):
    fs = factors(n)
    pr = 1
    for d, k in fs:
        pr *= (d ** (k + 1) - 1) // (d - 1)
    return pr


def rcpm(r, i, v):
    r = list(r)
    r[i] = v
    return r


OPS = {
    'addr': (lambda r, a, b, c: rcpm(r, c, r[a] + r[b])),
    'addi': (lambda r, a, b, c: rcpm(r, c, r[a] + b)),
    'mulr': (lambda r, a, b, c: rcpm(r, c, r[a] * r[b])),
    'muli': (lambda r, a, b, c: rcpm(r, c, r[a] * b)),
    'banr': (lambda r, a, b, c: rcpm(r, c, r[a] & r[b])),
    'bani': (lambda r, a, b, c: rcpm(r, c, r[a] & b)),
    'borr': (lambda r, a, b, c: rcpm(r, c, r[a] | r[b])),
    'bori': (lambda r, a, b, c: rcpm(r, c, r[a] | b)),
    'setr': (lambda r, a, b, c: rcpm(r, c, r[a])),
    'seti': (lambda r, a, b, c: rcpm(r, c, a)),
    'gtir': (lambda r, a, b, c: rcpm(r, c, int(a > r[b]))),
    'gtri': (lambda r, a, b, c: rcpm(r, c, int(r[a] > b))),
    'gtrr': (lambda r, a, b, c: rcpm(r, c, int(r[a] > r[b]))),
    'eqir': (lambda r, a, b, c: rcpm(r, c, int(a == r[b]))),
    'eqri': (lambda r, a, b, c: rcpm(r, c, int(r[a] == b))),
    'eqrr': (lambda r, a, b, c: rcpm(r, c, int(r[a] == r[b]))),
}


def simulate(instr, ipr, regs=None):
    regs = regs or [0] * 6

    while regs[ipr] < len(instr):
        op, a1, a2, a3 = instr[regs[ipr]]
        regs = OPS[op](regs, a1, a2, a3)
        regs[ipr] += 1

    return regs


def main():
    input = open('input').read().strip().split('\n')
    n2 = 10551425
    ipr = int(input[0].split()[1])
    instr = [
        (ls[0], int(ls[1]), int(ls[2]), int(ls[3]))
        for l in input[1:]
        for ls in [l.split()]
    ]

    s1 = simulate(instr, ipr)[0]
    s2 = divsum(n2)

    print(s1)
    print(s2)


main()
