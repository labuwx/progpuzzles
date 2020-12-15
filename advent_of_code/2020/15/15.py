#!/usr/bin/env python3

import itertools as it


def main():
    input = [int(x) for x in open('input').read().strip().split(',')]
    idx1 = 2020
    idx2 = 30000000

    last_heard = {n: i for i, n in enumerate(input[:-1])}
    m = input[-1]
    for i in it.count(len(input)):
        s = i - 1 - last_heard.get(m, i - 1)
        last_heard[m] = i - 1
        m = s
        if i == idx1 - 1:
            s1 = s
        if i == idx2 - 1:
            s2 = s
            break

    print(s1)
    print(s2)


main()
