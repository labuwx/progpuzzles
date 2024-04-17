#!/usr/bin/env python3

import itertools as it


def main():
    input = open('input').read().strip().split('\n')
    # input = open('input_test').read().strip().split('\n')

    symbols = []
    numbers = []
    for i, l in enumerate(input):
        nums = ''
        for j, c in enumerate(it.chain(l, ['.'])):
            if c.isdigit():
                nums += c
            else:
                if c != '.':
                    symbols.append((c, i, j))
                if nums != '':
                    l = len(nums)
                    numbers.append((int(nums), i, j - l, l))
                    nums = ''

    s1 = 0
    for n, i_n, j_n, l in numbers:
        for _, i_s, j_s in symbols:
            if i_n - 1 <= i_s <= i_n + 1 and j_n - 1 <= j_s <= j_n + l:
                s1 += n
                break

    s2 = 0
    for s, i_s, j_s in symbols:
        if s != '*':
            continue

        nc, st = 0, 1
        for n, i_n, j_n, l in numbers:
            if i_n - 1 <= i_s <= i_n + 1 and j_n - 1 <= j_s <= j_n + l:
                nc += 1
                st *= n
        if nc == 2:
            s2 += st

    print(s1)
    print(s2)


main()
