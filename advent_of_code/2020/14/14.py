#!/usr/bin/env python3

import functools as ft
import re


pattern = re.compile(
    r'(?P<type>mask|mem)(?: = (?P<mask>[01X]+)|\[(?P<addr>\d+)\] = (?P<val>\d+))'
)


def digits(n, *, padlen=None, b=10):
    ds = []
    while n:
        ds.append(n % b)
        n = n // b
    if ds == []:
        ds = [0]

    if padlen != None and len(ds) < padlen:
        ds += [0] * (padlen - len(ds))

    return tuple(reversed(ds))


def tonum(l, b=10):
    l = list(l)
    return ft.reduce(lambda acc, x: b * acc + x, l, 0)


def with_mask(n, mask):
    return zip(digits(n, b=2, padlen=len(mask)), mask)


def float_bits(bits):
    i = next((i for i, b in enumerate(bits) if b == None), None)
    if i == None:
        yield bits
    else:
        bits = list(bits)
        bits[i] = 0
        yield from float_bits(bits)
        bits[i] = 1
        yield from float_bits(bits)


def main():
    input = open('input').read().strip().split('\n')
    instr = []
    for l in input:
        m = pattern.match(l)
        if m['type'] == 'mask':
            mask = [int(c) if c != 'X' else None for c in m['mask']]
            instr.append(('mask', mask))
        else:
            addr = int(m['addr'])
            val = int(m['val'])
            instr.append(('mem', addr, val))

    memory = {}
    for type, *rest in instr:
        if type == 'mask':
            mask = rest[0]
        else:
            addr, val = rest
            fin_val = tonum(
                (b if m == None else m for b, m in with_mask(val, mask)), b=2
            )
            memory[addr] = fin_val
    s1 = sum(memory.values())

    memory = {}
    for type, *rest in instr:
        if type == 'mask':
            mask = rest[0]
        else:
            addr, val = rest
            mid_addr = [b if m == 0 else m for b, m in with_mask(addr, mask)]
            for fin_addr in float_bits(mid_addr):
                memory[tonum(fin_addr, b=2)] = val
    s2 = sum(memory.values())

    print(s1)
    print(s2)


main()
