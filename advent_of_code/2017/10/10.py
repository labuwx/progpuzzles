#!/usr/bin/env python3

import functools as ft


def rounder(input, nround=1):
    l = 256
    mem = list(range(l))
    idx = skip = 0
    for _ in range(nround):
        for n in input:
            for j in range(n // 2):
                i1 = (idx+j) % l
                i2 = (idx+n-1-j) % l
                mem[i1], mem[i2] = mem[i2], mem[i1]
            idx = (idx + n + skip) % l
            skip += 1
    return mem

################################################################################

input = open('input').read()
input = [int(num) for num in input.split(',')]

mem = rounder(input)
hash1 = mem[0] * mem[1]
print(hash1)

################################################################################

input = open('input').read().split('\n')[0]
input = list(map(ord, input))
input += [17, 31, 73, 47, 23]

mem = rounder(input, 64)
dense_mem = [ft.reduce(lambda x, y: x^y, mem[i*16: i*16+16]) for i in range(16)]

hash2 = ''.join('%0.2x' % x for x in dense_mem)
print(hash2)
