#!/usr/bin/env python3

import hashlib
import itertools as it


def md5(inp):
    inp = inp.encode('ascii')
    return hashlib.new('md5', inp).hexdigest()


def main():
    input = open('input').read().strip()
    pattern1 = '0' * 5
    pattern2 = '0' * 6

    s1 = next(x for x in it.count() if md5(input + str(x)).startswith(pattern1))
    s2 = next(x for x in it.count() if md5(input + str(x)).startswith(pattern2))

    print(s1)
    print(s2)


main()
