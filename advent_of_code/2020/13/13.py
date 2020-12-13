#!/usr/bin/env python3


def wait(time, bus):
    return bus - time % bus


def find_chinese(remainders):
    p, n = remainders[0]
    for q, m in remainders[1:]:
        n = next(l for l in (n + k * p for k in range(q)) if l % q == m)
        p *= q
    return n


def main():
    input = open('input').read().split()
    # input = open('input_test').read().split()
    T0 = int(input[0])
    buses = [int(c) if c != 'x' else None for c in input[1].split(',')]

    s1 = min((wait(T0, b), b) for b in buses if b != None)
    s1 = s1[0] * s1[1]

    rems = [(b, (-i % b)) for i, b in enumerate(buses) if b != None]
    s2 = find_chinese(rems)

    print(s1)
    print(s2)


main()
