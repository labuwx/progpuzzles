#!/usr/bin/env python3

import re


def find_chinese(remainders):
    p, n = remainders[0]
    for q, m in remainders[1:]:
        n = next(l for l in (n + k * p for k in range(q)) if l % q == m)
        p *= q
    return n


def rotate(npos, pos, t):
    return (pos + t) % npos


def discs_to_rem(discs):
    remainders = [
        (npos, (-(pos + i + 1) % npos)) for i, (npos, pos) in enumerate(discs)
    ]
    return remainders


pattern = re.compile(
    r'^Disc #(?P<disc>\d+) has (?P<npos>\d+) positions; at time=(?P<time>\d+), it is at position (?P<pos>\d+).$'
)


def main():
    input = open('input').read().strip()
    discs = []
    for i, l in enumerate(input.split('\n')):
        m = pattern.fullmatch(l)
        disc = int(m['disc'])
        assert disc == i + 1
        npos, t, pos = int(m['npos']), int(m['time']), int(m['pos'])
        pos0 = rotate(npos, pos, -t)
        discs.append((npos, pos0))

    rem1 = discs_to_rem(discs)
    rem2 = discs_to_rem(discs + [(11, 0)])

    s1 = find_chinese(rem1)
    s2 = find_chinese(rem2)

    print(s1)
    print(s2)


main()
