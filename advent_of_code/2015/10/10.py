#!/usr/bin/env python3


def step(seq):
    seq = seq + ' '
    nseq, run, cc = '', 0, seq[0]
    for c in seq:
        if c != cc:
            nseq += str(run) + cc
            run = 1
            cc = c
        else:
            run += 1

    return nseq


def it_step(seq, n=1):
    for _ in range(n):
        seq = step(seq)

    return seq


def main():
    input = open('input').read().strip()

    s1 = len(it_step(input, 40))
    s2 = len(it_step(input, 50))

    print(s1)
    print(s2)


main()
