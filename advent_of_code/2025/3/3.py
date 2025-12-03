#!/usr/bin/env python3


from collections import defaultdict


def main():
    input = open('input').read()
    # input = open('input_test').read()
    input = [[int(x) for x in l] for l in input.strip().splitlines()]
    m = 12

    s1 = s2 = 0
    for bank in input:
        M = defaultdict(int)
        for k in range(1, m + 1):
            for i in range(k, len(bank) + 1):
                v1 = M[(k, i - 1)]
                v2 = bank[-i] * 10 ** (k - 1) + M[(k - 1, i - 1)]
                M[(k, i)] = max(v1, v2)

        s1 += M[(2, len(bank))]
        s2 += M[(12, len(bank))]

    print(s1)
    print(s2)


main()
