#!/usr/bin/env python3

from collections import Counter


def main():
    input = [int(x) for x in open('input').read().split()]
    input = sorted(input)
    max_diff = 3
    devj = input[-1] + max_diff

    inp_ex = [0] + input + [devj]
    cc = Counter()
    for x, y in zip(inp_ex, inp_ex[1:]):
        cc[y - x] += 1
    s1 = cc[1] * cc[3]

    ways = (0,) * (max_diff - 1) + (1,)
    for j in range(1, devj + 1):
        ways = ways[1:] + ((j in inp_ex) * sum(ways),)
    s2 = ways[-1]

    print(s1)
    print(s2)


main()
