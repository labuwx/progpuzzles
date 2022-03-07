#!/usr/bin/env python3

from collections import Counter


def parse_input(input):
    template, rules = input.split('\n\n')
    rules = [(tuple(x[0]), x[1]) for l in rules.split('\n') for x in [l.split(' -> ')]]

    return template, rules


def score(pair_cnt, rightmost):
    elem_cnt = Counter({rightmost: 1})
    for pair, k in pair_cnt.items():
        if k > 0:
            elem_cnt[pair[0]] += k

    M = max(elem_cnt.values())
    m = min(elem_cnt.values())
    return M - m


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()
    n1, n2 = 10, 40

    template, rules = parse_input(input)
    pair_cnt = Counter(zip(template, template[1:]))

    for i in range(n2):
        new_pair_cnt = pair_cnt.copy()
        for pair, res_elem in rules:
            k = pair_cnt[pair]

            new_pair_cnt[pair] -= k
            new_pair_cnt[(pair[0], res_elem)] += k
            new_pair_cnt[(res_elem, pair[1])] += k

        pair_cnt = new_pair_cnt

        if i + 1 == n1:
            s1 = score(pair_cnt, template[-1])
    s2 = score(pair_cnt, template[-1])

    print(s1)
    print(s2)


main()
