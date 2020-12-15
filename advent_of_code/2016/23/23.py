#!/usr/bin/env python3

import re

tgl_map = {
    'inc': 'dec',
    'dec': 'inc',
    'tgl': 'inc',
    'jnz': 'cpy',
    'cpy': 'jnz',
}


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
    instr = [list(ins) for ins in instr]
    mem = {r: 0 for r in ['a', 'b', 'c', 'd']}
    mem.update({} if mem_init == None else mem_init)

    idx = 0
    while idx < len(instr):
        op, a1, a2 = instr[idx]

        if op == 'cpy':
            mem[a2] = mval(mem, a1)
        elif op == 'inc':
            mem[a1] += 1
        elif op == 'dec':
            mem[a1] -= 1
        elif op == 'tgl':
            ipn = idx + mval(mem, a1)
            if ipn < len(instr):
                fop = instr[ipn][0]
                instr[ipn][0] = tgl_map[fop]

        if op == 'jnz' and mval(mem, a1) != 0:
            idx += mval(mem, a2)
        else:
            idx += 1

    return dict(mem)


def main():
    input = open('input').read().strip()

    instr = []
    for line in input.split('\n'):
        if line == '':
            continue
        m = re.fullmatch(r'^(?P<op>\w+) (?P<a1>-?\w+)(?: (?P<a2>-?\w+))?$', line)
        op, a1, a2 = m.group('op'), m.group('a1'), m.group('a2')
        a1, a2 = myint(a1), myint(a2)
        instr.append((op, a1, a2))

    s1 = run(instr, {'a': 7})['a']
    s2 = run(instr, {'a': 12})['a']

    print(s1)
    print(s2)


main()
