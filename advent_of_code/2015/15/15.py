#!/usr/bin/env python3

import re
import sys
import numpy as np

# for dict to keep the order
assert sys.version_info >= (3, 7)


pattern = re.compile(
    r'^(?P<ing>\w+): capacity (?P<cap>-?\d+), durability (?P<dur>-?\d+), flavor (?P<flv>-?\d+), texture (?P<tex>-?\d+), calories (?P<cal>-?\d+)$'
)
prop_names = ('cap', 'dur', 'flv', 'tex', 'cal')


def score(xs):
    s = 1
    for x in xs[:-1]:
        s *= max(0, x)
    return s


def part_sum(total, nparts):
    if nparts == 1:
        yield (total,)
    else:
        for k in range(0, total + 1):
            for rest in part_sum(total - k, nparts - 1):
                yield (k,) + rest


def main():
    input = open('input').read().strip().split('\n')
    ingreds = {
        m['ing']: np.array([int(m[k]) for k in prop_names])
        for l in input
        for m in [pattern.fullmatch(l)]
    }
    max_ing = 100
    target_cal = 500

    score_max, score_max_lowcal = 0, -1
    for quants in part_sum(max_ing, len(ingreds)):
        mix = sum(q * ing for q, ing in zip(quants, ingreds.values()))

        sc = score(mix)
        score_max = max(score_max, sc)
        if mix[-1] == target_cal:
            score_max_lowcal = max(score_max_lowcal, sc)

    print(score_max)
    print(score_max_lowcal)


main()
