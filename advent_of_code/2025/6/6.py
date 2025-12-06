#!/usr/bin/env python3

import operator

opmap = {'+': operator.add, '*': operator.mul, ' ': None}
idenmap = {'+': 0, '*': 1}


def main():
    input = open('input').read()
    # input = open('input_test').read()

    A = [l.split() for l in input.strip().splitlines()]
    B = input.splitlines()

    s1 = 0
    for i in range(len(A[0])):
        t = 0 if A[-1][i] == '+' else 1
        for j in range(len(A) - 1):
            op = opmap[A[-1][i]]
            t = op(t, int(A[j][i]))
        s1 += t

    s2 = 0
    q = []
    for i in reversed(range(len(B[0]))):
        t = None
        for j in range(len(B) - 1):
            c = B[j][i]
            if c != ' ':
                if t is None:
                    t = 0
                t = 10 * t + int(c)
        if t is not None:
            q.append(t)

        if (op := opmap[B[-1][i]]) is not None:
            t = idenmap[B[-1][i]]
            while q:
                t = op(t, q.pop())
            s2 += t

    print(s1)
    print(s2)


main()
