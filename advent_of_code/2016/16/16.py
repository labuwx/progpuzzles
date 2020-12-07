#!/usr/bin/env python3

import itertools as it


def dragon(curve, min_len):
    while len(curve) < min_len:
        b = [(x + 1) % 2 for x in reversed(curve)]
        curve = curve + [0] + b
    return curve


def checksum(data):
    nlevel = next(i for i in it.count() if len(data) % 2 ** i != 0) - 1
    block_size = 2 ** nlevel
    csum = [1 if nlevel > 0 else 0] * (len(data) // block_size)
    for i, x in enumerate(data):
        block = i // block_size
        csum[block] = (csum[block] + x) % 2

    return csum


# def checksum(data):
    # while len(data) % 2 == 0:
        # data = [1 if x == y else 0 for x, y in zip(data[::2], data[1::2])]

     # return data


def cs_to_str(cs):
    return ''.join(str(x) for x in cs)


def main():
    input = [int(x) for x in open('input').read().strip()]
    l1, l2 = 272, 35651584

    curve1 = dragon(input, l1)
    s1 = checksum(curve1[:l1])

    curve2 = dragon(input, l2)
    s2 = checksum(curve2[:l2])

    print(cs_to_str(s1))
    print(cs_to_str(s2))


main()
