#!/usr/bin/env python3

import re


def tadd(x, y):
    return tuple(xx + yy for xx, yy in zip(x, y))


rx = r'''Button A: X\+(?P<AX>\d+), Y\+(?P<AY>\d+)
Button B: X\+(?P<BX>\d+), Y\+(?P<BY>\d+)
Prize: X=(?P<PX>\d+), Y=(?P<PY>\d+)'''

AP, BP = 3, 1
OFFSET = (10000000000000, 10000000000000)


# assumes that {a, b} is a basis in R^2
def solve(a, b, p):
    ta_n = p[0] * b[1] - p[1] * b[0]
    ta_d = a[0] * b[1] - a[1] * b[0]
    tb_n = -p[0] * a[1] + p[1] * a[0]
    tb_d = a[0] * b[1] - a[1] * b[0]

    if (
        ta_n % ta_d
        or tb_n % tb_d
        or (ta := ta_n // ta_d) < 0
        or (tb := tb_n // tb_d) < 0
    ):
        return None

    return ta, tb


def main():
    input = open('input').read()
    # input = open('input_test').read()

    l = [
        (
            (int(m['AX']), int(m['AY'])),
            (int(m['BX']), int(m['BY'])),
            (int(m['PX']), int(m['PY'])),
        )
        for m in re.finditer(rx, input)
    ]

    s1 = s2 = 0
    for a, b, p in l[:]:
        if (t := solve(a, b, p)) is not None:
            s1 += t[0] * AP + t[1] * BP
        if (t := solve(a, b, tadd(p, OFFSET))) is not None:
            s2 += t[0] * AP + t[1] * BP

    print(s1)
    print(s2)


main()
