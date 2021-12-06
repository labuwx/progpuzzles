#!/usr/bin/env python3

from collections import Counter
import re

pattern = re.compile(r'(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)')


def srange(p1, p2):
    x_inc = p2[0] - p1[0]
    y_inc = p2[1] - p1[1]
    nsteps = max(abs(x_inc), abs(y_inc))
    x_inc //= nsteps
    y_inc //= nsteps

    x, y = p1
    for _ in range(nsteps + 1):
        yield x, y
        x += x_inc
        y += y_inc


def main():
    input = open('input').read().strip()
    data = [
        ((int(m['x1']), int(m['y1'])), (int(m['x2']), int(m['y2'])))
        for m in pattern.finditer(input)
    ]

    hv_lines, diag_lines = Counter(), Counter()
    for p1, p2 in data:
        c = hv_lines if p1[0] == p2[0] or p1[1] == p2[1] else diag_lines
        for p in srange(p1, p2):
            c[p] += 1

    s1 = sum(k > 1 for k in hv_lines.values())
    s2 = sum(k > 1 for k in (hv_lines + diag_lines).values())

    print(s1)
    print(s2)


main()
