#!/usr/bin/env python3


def parse_inp(txt):
    p1, p2 = txt.strip().split('\n\n')
    rules = {tuple(int(x) for x in l.split('|')) for l in p1.splitlines()}
    updates = [[int(x) for x in l.split(',')] for l in p2.splitlines()]

    return rules, updates


def mid(l):
    return l[len(l) // 2]


def check(rules, upd):
    return all(xy in rules for xy in zip(upd, upd[1:]))


def fixedmid(rules, upd):
    n = len(upd)
    pos = lambda y: sum((x, y) in rules for x in upd)

    midx = next(x for x in upd if pos(x) == n // 2)

    return midx


def main():
    input = open('input').read()
    # input = open('input_test').read()

    rules, updates = parse_inp(input)

    bad, good = [], []
    for upd in updates:
        (bad, good)[check(rules, upd)].append(upd)

    s1 = sum(mid(upd) for upd in good)
    s2 = sum(fixedmid(rules, upd) for upd in bad)

    print(s1)
    print(s2)


main()
