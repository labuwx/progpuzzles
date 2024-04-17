#!/usr/bin/env python3

from collections import defaultdict


def parse_nums(s):
    return (int(ns) for ns in s.split())


def main():
    input = open('input').read().strip().split('\n')
    # input = open('input_test').read().strip().split('\n')

    cards = []
    for i, l in enumerate(input):
        wp, tp = l.split(':')[1].split('|')
        w_n = set(parse_nums(wp))
        t_n = set(parse_nums(tp))
        wins = len(w_n & t_n)
        cards.append(wins)

    s1 = s2 = 0
    rewins = defaultdict(lambda: 1)
    for i, wins in enumerate(cards):
        s2 += rewins[i]
        if wins:
            s1 += 2 ** (wins - 1)
        for k in range(wins):
            rewins[i + k + 1] += rewins[i]

    print(s1)
    print(s2)


main()
