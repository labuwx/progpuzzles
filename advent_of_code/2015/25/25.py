#!/usr/bin/env python3

import re


pattern = re.compile(
    r'To continue, please consult the code grid in the manual\.  Enter the code at row (?P<row>\d+), column (?P<col>\d+)\.'
)


def diag_to_n(pos):
    x, y = pos
    diag = x + y - 1
    num_before_diag = (diag * (diag - 1)) // 2
    n = num_before_diag + x
    return n


def main():
    init_val, base, mod = 20151125, 252533, 33554393
    input = open('input').read().strip()
    minput = pattern.fullmatch(input)
    pos = int(minput['col']), int(minput['row'])

    n = diag_to_n(pos)
    s1 = (init_val * pow(base, n - 1, mod)) % mod

    print(s1)


main()
