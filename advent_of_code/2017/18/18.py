#!/usr/bin/env python3

import re
from collections import defaultdict, deque


def myint(x):
    try:
        res = int(x)
    except:
        res = x

    return res

def mval(mem, x):
    assert x != None
    return x if isinstance(x, int) else mem[x]

def mpop(stack):
    try:
        x = stack.popleft()
    except:
        x = None
    return x


input = open('input').read()

instr = []
for line in input.split('\n'):
    if line == '': continue
    m = re.match(r'^(?P<op>\w+) (?P<a1>-?\w+)( (?P<a2>-?\w+))?$', line)
    op, a1, a2 = m.group('op'), m.group('a1'), m.group('a2')
    a1, a2 = myint(a1), myint(a2)
    instr.append((op, a1, a2))

mem = defaultdict(int)
idx, last_snd = 0, None
while idx < len(instr):
    op, a1, a2 = instr[idx]
    if op == 'snd':
        last_snd = mval(mem, a1)
    elif op == 'set':
        mem[a1] = mval(mem, a2)
    elif op == 'add':
        mem[a1] += mval(mem, a2)
    elif op == 'mul':
        mem[a1] *= mval(mem, a2)
    elif op == 'mod':
        mem[a1] %= mval(mem, a2)
    elif op == 'rcv':
        if mem[a1] != 0:
            fst_snd = last_snd
            mem[a1] = last_snd
            break
    if op == 'jgz' and mval(mem, a1) > 0:
        idx += mval(mem, a2)
    else:
        idx += 1

print(fst_snd)


n = 2
gmem = [defaultdict(int, {'p': i}) for i in range(n)]
stack = [deque() for _ in range(n)]
idx = [0] * n
deadlock, c = False, 0
while not deadlock:
    deadlock = True
    for j in range(n):
        mem = gmem[j]
        if idx[j] >= len(instr): continue
        op, a1, a2 = instr[idx[j]]
        if op == 'snd':
            if j == 1:
                c += 1
            stack[j].append(mval(mem, a1))
        elif op == 'set':
            mem[a1] = mval(mem, a2)
        elif op == 'add':
            mem[a1] += mval(mem, a2)
        elif op == 'mul':
            mem[a1] *= mval(mem, a2)
        elif op == 'mod':
            mem[a1] %= mval(mem, a2)
        elif op == 'rcv':
            x = mpop(stack[(j+1)%n])
            if x == None:
                continue
            else:
                mem[a1] = x
        if op == 'jgz' and mval(mem, a1) > 0:
            idx[j] += mval(mem, a2)
        else:
            idx[j] += 1
        deadlock = False

print(c)
