#!/usr/bin/env python3

from collections import defaultdict
import itertools as it
import re
import operator


BW = 16
OPS = {
    'AND': operator.__and__,
    'OR': operator.__or__,
    'NOT': (lambda x: (2 ** BW - 1) ^ x),
    'LSHIFT': (lambda x, y: (x << y) % (2 ** BW)),
    'RSHIFT': operator.rshift,
    'ID': (lambda x: x),
}


def parse(code):
    prog = []
    for l in code:
        r = {'dst': l[-1], 'src': [], 'op': OPS['ID']}
        for token in l:
            if token == '->':
                break
            elif token in OPS:
                r['op'] = OPS[token]
            elif token.isdigit():
                r['src'].append(int(token))
            else:
                r['src'].append(token)

        prog.append(r)

    return prog


def execute(prog, vals=None):
    vals = dict(vals if vals else {})
    prog = {instr['dst']: instr for instr in prog}
    stack = list(prog.keys())

    while stack:
        dst = stack[-1]
        p = prog[dst]

        if dst in vals:
            stack.pop()
            continue

        args = []
        for src in p['src']:
            if isinstance(src, int):
                args.append(src)
            elif src in vals:
                args.append(vals[src])
            else:
                stack.append(src)

        if dst != stack[-1]:
            continue
        else:
            vals[dst] = p['op'](*args)
            stack.pop()

    return vals


def main():
    input = [l.split() for l in open('input').read().strip().split('\n')]
    prog = parse(input)

    s1 = execute(prog)['a']
    s2 = execute(prog, {'b': s1})['a']

    print(s1)
    print(s2)


main()
