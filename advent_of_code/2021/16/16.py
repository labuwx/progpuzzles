#!/usr/bin/env python3

import math


class Packet:
    def __init__(self, version, type, *, value=None, subs=None):
        self.version = version
        self.type = type
        self.value = value
        self.subs = [] if subs is None else subs

        # print(f"Packet:\n    {version}\n    {type}\n    {value}\n    {len(self.subs)}")


def hex2bits(hs):
    bits = [int(x) for x in bin(int(hs, 16))[2:].zfill(4 * len(hs))]
    return bits


def bits2num(bits):
    x = sum(b * 2**i for i, b in enumerate(reversed(bits)))
    return x


def parse(bits):
    idx = 0

    def consume(nbits=1):
        nonlocal idx
        v = bits[idx : idx + nbits]
        idx += nbits
        return v

    def parse_inner():
        nonlocal idx
        version = bits2num(consume(3))
        type = bits2num(consume(3))

        if type == 4:
            value = 0
            while True:
                last_block = not consume()[0]
                value = value * 2**4 + bits2num(consume(4))
                if last_block:
                    break
            return Packet(version, type, value=value)

        else:
            ltid = consume()[0]

            if ltid == 0:
                nsubbits = bits2num(consume(15))
                idx_0 = idx
                subs = []
                while idx - idx_0 < nsubbits:
                    subs.append(parse_inner())

            else:  # ltid == 1
                nsubs = bits2num(consume(11))
                subs = [parse_inner() for _ in range(nsubs)]

            return Packet(version, type, subs=subs)

    return parse_inner()


def version_sum(p, subvals):
    return p.version + sum(subvals)


def peval(p, subvals):
    match p.type:
        case 0:
            v = sum(subvals)
        case 1:
            v = math.prod(subvals)
        case 2:
            v = min(subvals)
        case 3:
            v = max(subvals)
        case 4:
            v = p.value
        case 5:
            v = int(subvals[0] > subvals[1])
        case 6:
            v = int(subvals[0] < subvals[1])
        case 7:
            v = int(subvals[0] == subvals[1])
    return v


def traverse(f, p):
    subvals = [traverse(f, subp) for subp in p.subs]
    return f(p, subvals)


def main():
    input = open('input').read().strip()
    bits = hex2bits(input)
    rootp = parse(bits)

    s1 = traverse(version_sum, rootp)
    s2 = traverse(peval, rootp)

    print(s1)
    print(s2)


main()
