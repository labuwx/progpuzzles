#!/usr/bin/env python3

from collections import deque
import math
from operator import lt, gt
import re


rex_rule = re.compile(r'((?P<cat>[xmas])(?P<cmp>[<>])(?P<val>\d+):)?(?P<to>\w+)')


def parse_input(input):
    input = input.strip().split('\n\n')

    rules = {}
    for rl in input[0].splitlines():
        name, rl = rl.split('{')
        rules[name] = []
        for rp in rl[:-1].split(','):
            m = rex_rule.fullmatch(rp)
            to, cat, cmp, val = m['to'], m['cat'], m['cmp'], m['val']
            if cmp is not None:
                val = int(val)
                cmp = lt if cmp == '<' else gt
            rules[name].append((to, cat, cmp, val))

    parts = []
    for pl in input[1].splitlines():
        part = {}
        for prop in pl[1:-1].split(','):
            name, val = prop.split('=')
            part[name] = int(val)
        parts.append(part)

    return rules, parts


def isvalid(M, r):
    return 1 <= r[0] <= r[1] <= M


def main():
    input = open('input').read()
    # input = open('input_test').read()
    M = 4000

    rules, parts = parse_input(input)

    s1 = 0
    for part in parts:
        wf = 'in'
        decision = None
        while decision is None:

            for to, cat, cmp, val in rules[wf]:
                if cmp is None or cmp(part[cat], val):
                    if to in 'AR':
                        decision = to == 'A'
                    wf = to
                    break

        if decision:
            s1 += sum(part.values())

    s2 = 0
    q = deque([({c: (1, M) for c in 'xmas'}, 'in', 0)])
    while q:
        part, wf, k = q.pop()
        if wf in 'AR':
            s2 += math.prod(X - x + 1 for x, X in part.values()) if wf == 'A' else 0
            continue

        to, cat, cmp, val = rules[wf][k]

        if cmp is None:
            q.append((part, to, 0))
            continue

        part_m = dict(part)
        x, X = part[cat]

        if cmp == lt:
            part_m[cat] = (x, val - 1)
            part[cat] = (val, X)
        else:
            part_m[cat] = (val + 1, X)
            part[cat] = (x, val)

        if isvalid(M, part[cat]):
            q.append((part, wf, k + 1))

        if isvalid(M, part_m[cat]):
            q.append((part_m, to, 0))

    print(s1)
    print(s2)


main()
