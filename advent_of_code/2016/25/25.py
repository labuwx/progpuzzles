#!/usr/bin/env python3

from collections import defaultdict
import itertools as it
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
    mem = defaultdict(int, {} if mem_init == None else mem_init)

    idx = 0
    while idx < len(instr):
        op, a1, a2 = instr[idx]
        if op == 'cpy':
            mem[a2] = mval(mem, a1)
        elif op == 'inc':
            mem[a1] += 1
        elif op == 'dec':
            mem[a1] -= 1
        elif op == 'out':
            yield mval(mem, a1)

        if op == 'jnz' and mval(mem, a1) != 0:
            idx += mval(mem, a2)
        else:
            idx += 1

    return dict(mem)


def main():
    input = open('input').read().strip()
    testlen = 50

    instr = []
    for line in input.split('\n'):
        if line == '':
            continue
        m = re.fullmatch(r'^(?P<op>\w+) (?P<a1>-?\w+)(?: (?P<a2>-?\w+))?$', line)
        op, a1, a2 = m.group('op'), m.group('a1'), m.group('a2')
        a1, a2 = myint(a1), myint(a2)
        instr.append((op, a1, a2))

    machines, s1 = {}, None
    for a in it.count():
        if s1 != None:
            break
        machines[a] = run(instr, {'a': a})
        ms = set(machines.keys())
        for aa in ms:
            m = machines[aa]
            x = next(m, None)
            if x == (a + aa) % 2:
                if a - aa > testlen:
                    s1 = aa
                    break
            else:
                del machines[aa]

    print(s1)


main()
