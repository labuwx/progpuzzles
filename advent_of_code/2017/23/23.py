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

def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


input = open('input').read()

instr = []
for line in input.split('\n'):
    if line == '': continue
    m = re.match(r'^(?P<op>\w+) (?P<a1>-?\w+)( (?P<a2>-?\w+))?$', line)
    op, a1, a2 = m.group('op'), m.group('a1'), m.group('a2')
    a1, a2 = myint(a1), myint(a2)
    instr.append((op, a1, a2))


mem = defaultdict(int)
idx, cmul = 0, 0
while idx < len(instr):
    op, a1, a2 = instr[idx]
    if op == 'set':
        mem[a1] = mval(mem, a2)
    elif op == 'sub':
        mem[a1] -= mval(mem, a2)
    elif op == 'mul':
        cmul += 1
        mem[a1] *= mval(mem, a2)
    if op == 'jnz' and mval(mem, a1) != 0:
        idx += mval(mem, a2)
    else:
        idx += 1
print(cmul)


b = 109900
c = 126900
h = 0
while b != c + 17:
    if not isprime(b):
        h += 1
    b += 17

print(h)
