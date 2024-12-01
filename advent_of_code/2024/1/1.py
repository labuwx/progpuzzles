#!/usr/bin/env python3

from collections import Counter


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = [tuple(int(x) for x in l.split()) for l in input.strip().splitlines()]

    l1 = sorted(p[0] for p in input)
    l2 = sorted(p[1] for p in input)
    c2 = Counter(l2)

    s1 = sum(abs(x1 - x2) for x1, x2 in zip(l1, l2))
    s2 = sum(x * c2[x] for x in l1)

    print(s1)
    print(s2)


main()
