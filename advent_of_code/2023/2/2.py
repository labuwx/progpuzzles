#!/usr/bin/env python3

import re


rex_templ = r'\d+(?= %s)'
rex_rgb = [re.compile(rex_templ % color) for color in 'rgb']


def tcomp_le(at, bt):
    return all(a <= b for a, b in zip(at, bt))


def imult(l):
    p = 1
    for x in l:
        p *= x
    return p


def main():
    input = open('input').read().strip().split('\n')
    # input = open('input_test').read().strip().split('\n')

    test1 = (12, 13, 14)

    s1 = s2 = 0
    for i, l in enumerate(input):
        gameid = i + 1
        cmax = tuple(
            max((int(x.group(0)) for x in rex_c.finditer(l)), default=0)
            for rex_c in rex_rgb
        )
        if tcomp_le(cmax, test1):
            s1 += gameid
        s2 += imult(cmax)

    print(s1)
    print(s2)


main()
