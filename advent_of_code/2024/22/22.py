#!/usr/bin/env python3


from collections import defaultdict


def h(x):
    x = (x ^ (x * 64)) % 16777216
    x = (x ^ (x // 32)) % 16777216
    x = (x ^ (x * 2048)) % 16777216
    return x


def main():
    input = open('input').read()
    # input = open('input_test_1').read()
    # input = open('input_test_2').read()
    inits = [int(x) for x in input.strip().splitlines()]

    s1 = 0
    changes_prices = defaultdict(dict)
    for i, x in enumerate(inits):
        sq = tuple()
        p = x % 10
        for _ in range(2000):
            x = h(x)
            pn = x % 10
            sq = sq[-3:] + (pn - p,)
            p = pn
            if len(sq) == 4 and i not in changes_prices[sq]:
                changes_prices[sq][i] = p
        s1 += x

    s2 = max(sum(prices.values()) for prices in changes_prices.values())

    print(s1)
    print(s2)


main()
