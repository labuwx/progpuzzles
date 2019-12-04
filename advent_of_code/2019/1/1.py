#!/usr/bin/env python3


def f1(m):
    return max(m // 3 - 2, 0)


def f2(m):
    s, la = 0, m
    while la > 0:
        la = f1(la)
        s += la
    return s


def main():
    input = open('input').read()
    input = [int(x) for x in input.split()]

    s1 = sum(f1(m) for m in input)
    s2 = sum(f2(m) for m in input)

    print(s1)
    print(s2)


main()
