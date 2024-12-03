#!/usr/bin/env python3

import re


def main():
    input = open('input').read()
    # input = open('input_test_1').read()
    # input = open('input_test_2').read()
    input = input.strip()

    r = r"""(?P<mul>  mul\((?P<X>\d+),(?P<Y>\d+)\) )|
            (?P<do>   do\(\)                       )|
            (?P<dont> don't\(\)                    )"""

    s1 = s2 = 0
    enabled = True
    for m in re.finditer(r, input, flags=re.VERBOSE):
        enabled = (enabled or (m['do'] is not None)) and (m['dont'] is None)
        if m['mul']:
            t = int(m['X']) * int(m['Y'])
            s1 += t
            s2 += enabled * t

    print(s1)
    print(s2)


main()
