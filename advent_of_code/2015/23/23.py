#!/usr/bin/env python3

import re


def myint(x):
    try:
        res = int(x)
    except:
        res = x

    return res


def mval(mem, x):
    assert x != None
    return x if isinstance(x, int) else mem[x]


def run(instr, mem_init=None):
    mem = {'a': 0, 'b': 0}
    if mem_init != None:
        mem.update(mem_init)

    idx = 0
    while idx < len(instr):
        op, a1, a2 = instr[idx]

        if op == 'hlf':
            mem[a1] //= 2
        elif op == 'tpl':
            mem[a1] *= 3
        elif op == 'inc':
            mem[a1] += 1

        if op == 'jmp':
            idx += a1
        elif (op == 'jie' and mem[a1] % 2 == 0) or (op == 'jio' and mem[a1] == 1):
            idx += a2
        else:
            idx += 1

    return mem


def main():
    input = open('input').read().strip()

    instr = []
    for line in input.split('\n'):
        m = re.fullmatch(r'^(?P<op>\w+) (?P<a1>[-+]?\w+)(?:, (?P<a2>[-+]?\w+))?$', line)
        op, a1, a2 = m.group('op'), m.group('a1'), m.group('a2')
        a1, a2 = myint(a1), myint(a2)
        instr.append((op, a1, a2))

    s1 = run(instr)['b']
    s2 = run(instr, {'a': 1})['b']

    print(s1)
    print(s2)


main()
