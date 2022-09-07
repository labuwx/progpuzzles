#!/usr/bin/env python3

from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import itertools as it
from typing import Optional, Union


@dataclass
class Number:
    p: Optional(Number) = None
    v: Optional(int) = None
    l: Optional(Union(Number, int)) = None
    r: Optional(Union(Number, int)) = None

    def __init__(self, *args):
        match len(args):
            case 1:
                (self.p,) = args
            case 2:
                self.p, self.v = args
            case 3:
                self.p, self.l, self.r = args
            case other:
                assert False

    def __str__(self):
        if self.v is None:
            return "[" + str(self.l) + ', ' + str(self.r) + "]"
        else:
            return str(self.v)

    def is_num(self):
        return self.v is not None


def parse_number(s):
    idx = 0

    def consume(n=1):
        nonlocal idx
        v = s[idx : idx + n]
        idx += n
        return v

    def inner_parser(parent=None):
        nonlocal idx
        type = s[idx]

        if type == '[':
            v = Number(parent)
            consume()  # [
            v.l = inner_parser(v)
            consume()  # ,
            v.r = inner_parser(v)
            consume()  # ]

        else:
            v = 0
            while s[idx] in '0123456789':
                v = v * 10 + int(consume())
            v = Number(parent, v)

        return v

    return inner_parser()


def parse_input(input):
    numbers = [parse_number(l) for l in input.split('\n')]
    return numbers


def find_nb(num, side):
    while num.p != None and (num.p.r if side else num.p.l) is num:
        num = num.p

    if num.p == None:
        return None

    num = num.p.r if side else num.p.l

    while not num.is_num():
        num = num.l if side else num.r

    return num


def reduce(v):
    change = True
    while change:
        change = False

        # explode
        q = [(v, 0)]
        while q:
            x, d = q.pop()
            if d == 4 and not x.is_num():
                change = True
                break
            if x.is_num():
                continue
            q.extend([(x.r, d + 1), (x.l, d + 1)])

        if change:
            assert x.l.is_num() and x.r.is_num()
            if (lnb := find_nb(x, side=0)) is not None:
                lnb.v += x.l.v
            if (rnb := find_nb(x, side=1)) is not None:
                rnb.v += x.r.v
            x.l = x.r = None
            x.v = 0
            continue

        # split
        q = [v]
        while q:
            x = q.pop()
            if x.is_num() and x.v >= 10:
                change = True
                break
            if x.is_num():
                continue
            q.extend([x.r, x.l])

        if change:
            x.l = Number(x, x.v // 2)
            x.r = Number(x, x.v - x.v // 2)
            x.v = None
            continue


def add(x, y):
    v = Number(None, deepcopy(x), deepcopy(y))
    v.l.p = v.r.p = v
    reduce(v)
    return v


def add_l(xs):
    x = xs[0]
    for i, y in enumerate(xs[1:]):
        x = add(x, y)
    return x


def magnitude(x):
    if x.is_num():
        return x.v
    else:
        return 3 * magnitude(x.l) + 2 * magnitude(x.r)


def main():
    input = open('input').read().strip()
    # input = open('input_test').read().strip()
    numbers = parse_input(input)

    s1 = magnitude(add_l(numbers))
    s2 = max(magnitude(add(x, y)) for x, y in it.permutations(numbers, r=2))

    print(s1)
    print(s2)


main()
