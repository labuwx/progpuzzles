#!/usr/bin/env python3


import sys

OPS = {
    'addr': {'rt': (1, 1), 's': r'%(a3)s = %(a1)s + %(a2)s'},
    'addi': {'rt': (1, 0), 's': r'%(a3)s = %(a1)s + %(a2)s'},
    'mulr': {'rt': (1, 1), 's': r'%(a3)s = %(a1)s * %(a2)s'},
    'muli': {'rt': (1, 0), 's': r'%(a3)s = %(a1)s * %(a2)s'},
    'banr': {'rt': (1, 1), 's': r'%(a3)s = %(a1)s & %(a2)s'},
    'bani': {'rt': (1, 0), 's': r'%(a3)s = %(a1)s & %(a2)s'},
    'borr': {'rt': (1, 1), 's': r'%(a3)s = %(a1)s | %(a2)s'},
    'bori': {'rt': (1, 0), 's': r'%(a3)s = %(a1)s | %(a2)s'},
    'setr': {'rt': (1, None), 's': r'%(a3)s = %(a1)s'},
    'seti': {'rt': (0, None), 's': r'%(a3)s = %(a1)s'},
    'gtir': {'rt': (0, 1), 's': r'%(a3)s = int(%(a1)s > %(a2)s)'},
    'gtri': {'rt': (1, 0), 's': r'%(a3)s = int(%(a1)s > %(a2)s)'},
    'gtrr': {'rt': (1, 1), 's': r'%(a3)s = int(%(a1)s > %(a2)s)'},
    'eqir': {'rt': (0, 1), 's': r'%(a3)s = int(%(a1)s == %(a2)s)'},
    'eqri': {'rt': (1, 0), 's': r'%(a3)s = int(%(a1)s == %(a2)s)'},
    'eqrr': {'rt': (1, 1), 's': r'%(a3)s = int(%(a1)s == %(a2)s)'},
}


def main():
    inp_f = sys.argv[1] if len(sys.argv) == 2 else 'input'
    input = open(inp_f).read().strip().split('\n')
    ipr = int(input[0].split()[1])
    instr = [
        (ls[0], int(ls[1]), int(ls[2]), int(ls[3]))
        for l in input[1:]
        for ls in [l.split()]
    ]

    reg_names = ['ra', 'rb', 'rc', 'rd', 're']
    reg_names.insert(ipr, 'ip')
    for i, (op, a1, a2, a3) in enumerate(instr):
        code = OPS[op]['s']
        rtypes = OPS[op]['rt']
        ta1 = (str(i) if a1 == ipr else reg_names[a1]) if rtypes[0] else str(a1)
        ta2 = (str(i) if a2 == ipr else reg_names[a2]) if rtypes[1] else str(a2)
        ta3 = reg_names[a3]
        print(f'{i:>2}:    ', code % {'a1': ta1, 'a2': ta2, 'a3': ta3})


main()
