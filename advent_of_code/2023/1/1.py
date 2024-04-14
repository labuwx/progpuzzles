#!/usr/bin/env python3

import regex as re


digits_1 = [str(i) for i in range(1, 10)]
digits_s = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits_2 = digits_1 + digits_s

digitmap = {d: int(d) for d in digits_1} | {d: i + 1 for i, d in enumerate(digits_s)}
digit_rex = re.compile('(' + '|'.join(digits_2) + ')')


def main():
    input = open('input').read().split()
    # input = open('input_test').read().split()

    s1 = sum(
        int(''.join(next(c for c in x if c.isdigit()) for x in (l, reversed(l))))
        for l in input
    )

    s2 = 0
    for l in input:
        ldigits = digit_rex.findall(l, overlapped=True)
        s2 += 10 * digitmap[ldigits[0]] + digitmap[ldigits[-1]]

    print(s1)
    print(s2)


main()
